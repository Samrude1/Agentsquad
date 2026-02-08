"""
Rate limiting middleware for API protection.

Designed for portfolio demo with recruiter-friendly limits:
- Allows thorough testing of all features
- Prevents API abuse and cost overruns
- Provides clear feedback when limits are reached
"""

from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from datetime import datetime, timedelta
from collections import defaultdict
from typing import Dict, Tuple
import time


class RateLimiter:
    """
    In-memory rate limiter for demo purposes.
    For production, consider Redis-backed solution.
    """
    
    def __init__(self):
        # Store: {ip_address: [(timestamp, endpoint), ...]}
        self.requests: Dict[str, list] = defaultdict(list)
        
        # Rate limits optimized for recruiter testing
        self.limits = {
            # Agent endpoints - allow thorough testing but prevent abuse
            "agent": {
                "per_15min": 5,   # 5 agent runs per 15 minutes (test all 3 agents + retries)
                "per_hour": 10,   # 10 agent runs per hour
                "per_day": 25,    # 25 agent runs per day (generous for demo)
            },
            # Auth and general endpoints - more permissive
            "general": {
                "per_minute": 30,  # 30 requests per minute
                "per_hour": 500,   # 500 requests per hour
            }
        }
    
    def _clean_old_requests(self, ip: str, cutoff_time: datetime):
        """Remove requests older than cutoff time."""
        if ip in self.requests:
            self.requests[ip] = [
                (ts, endpoint) for ts, endpoint in self.requests[ip]
                if ts > cutoff_time
            ]
    
    def _count_requests(self, ip: str, since: datetime, endpoint_type: str = None) -> int:
        """Count requests from IP since given time, optionally filtered by endpoint type."""
        if ip not in self.requests:
            return 0
        
        if endpoint_type:
            return sum(
                1 for ts, ep in self.requests[ip]
                if ts > since and ep == endpoint_type
            )
        return sum(1 for ts, _ in self.requests[ip] if ts > since)
    
    def check_rate_limit(self, ip: str, endpoint_type: str = "general") -> Tuple[bool, str]:
        """
        Check if request should be allowed.
        
        Args:
            ip: Client IP address
            endpoint_type: "agent" or "general"
            
        Returns:
            (allowed: bool, message: str)
        """
        now = datetime.now()
        
        # Clean up old requests (older than 24 hours)
        self._clean_old_requests(ip, now - timedelta(days=1))
        
        if endpoint_type == "agent":
            limits = self.limits["agent"]
            
            # Check 15-minute limit
            count_15min = self._count_requests(ip, now - timedelta(minutes=15), "agent")
            if count_15min >= limits["per_15min"]:
                return False, f"Rate limit exceeded: {limits['per_15min']} agent requests per 15 minutes. Please wait before trying again."
            
            # Check hourly limit
            count_hour = self._count_requests(ip, now - timedelta(hours=1), "agent")
            if count_hour >= limits["per_hour"]:
                return False, f"Rate limit exceeded: {limits['per_hour']} agent requests per hour. Please try again later."
            
            # Check daily limit
            count_day = self._count_requests(ip, now - timedelta(days=1), "agent")
            if count_day >= limits["per_day"]:
                return False, f"Daily rate limit exceeded: {limits['per_day']} agent requests per day. Please try again tomorrow."
        
        else:  # general endpoints
            limits = self.limits["general"]
            
            # Check per-minute limit
            count_minute = self._count_requests(ip, now - timedelta(minutes=1))
            if count_minute >= limits["per_minute"]:
                return False, "Too many requests. Please slow down."
            
            # Check hourly limit
            count_hour = self._count_requests(ip, now - timedelta(hours=1))
            if count_hour >= limits["per_hour"]:
                return False, "Hourly rate limit exceeded. Please try again later."
        
        return True, "OK"
    
    def record_request(self, ip: str, endpoint_type: str = "general"):
        """Record a successful request."""
        self.requests[ip].append((datetime.now(), endpoint_type))
    
    def get_usage_stats(self, ip: str) -> dict:
        """Get current usage statistics for an IP (useful for debugging/monitoring)."""
        now = datetime.now()
        
        return {
            "agent_requests": {
                "last_15min": self._count_requests(ip, now - timedelta(minutes=15), "agent"),
                "last_hour": self._count_requests(ip, now - timedelta(hours=1), "agent"),
                "last_day": self._count_requests(ip, now - timedelta(days=1), "agent"),
            },
            "total_requests": {
                "last_minute": self._count_requests(ip, now - timedelta(minutes=1)),
                "last_hour": self._count_requests(ip, now - timedelta(hours=1)),
            },
            "limits": self.limits
        }


# Global rate limiter instance
rate_limiter = RateLimiter()


async def rate_limit_middleware(request: Request, call_next):
    """
    Middleware to apply rate limiting to all requests.
    """
    # Get client IP
    client_ip = request.client.host
    
    # Determine endpoint type
    path = request.url.path
    endpoint_type = "agent" if any(x in path for x in ["/api/sales/", "/api/research", "/api/meeting-prep"]) else "general"
    
    # Skip rate limiting for health checks and static files
    if path in ["/", "/health", "/api/config/auth-enabled"]:
        return await call_next(request)
    
    # Check rate limit
    allowed, message = rate_limiter.check_rate_limit(client_ip, endpoint_type)
    
    if not allowed:
        return JSONResponse(
            status_code=429,
            content={
                "error": "Rate limit exceeded",
                "message": message,
                "type": endpoint_type,
                "hint": "This is a demo application with usage limits to prevent abuse. Thank you for understanding!"
            }
        )
    
    # Record the request
    rate_limiter.record_request(client_ip, endpoint_type)
    
    # Continue with the request
    response = await call_next(request)
    
    # Add rate limit headers for transparency
    stats = rate_limiter.get_usage_stats(client_ip)
    if endpoint_type == "agent":
        response.headers["X-RateLimit-Remaining-15min"] = str(
            rate_limiter.limits["agent"]["per_15min"] - stats["agent_requests"]["last_15min"]
        )
        response.headers["X-RateLimit-Remaining-Day"] = str(
            rate_limiter.limits["agent"]["per_day"] - stats["agent_requests"]["last_day"]
        )
    
    return response
