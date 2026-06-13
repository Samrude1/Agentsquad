import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from typing import Dict
from agents import function_tool

def _send_email_raw(to_email: str, subject: str, html_body: str) -> Dict[str, str]:
    """Raw email sending function (for direct API calls)."""
    try:
        api_key = os.environ.get('SENDGRID_API_KEY')
        if not api_key:
            return {"status": "error", "message": "SENDGRID_API_KEY is not set."}
            
        from_email = os.environ.get('SENDER_EMAIL', "info@samirautanen.fi")
        
        message = Mail(
            from_email=from_email,
            to_emails=to_email,
            subject=subject,
            html_content=html_body
        )
        
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        
        print(f"SendGrid success: {response.status_code}")
        return {"status": "success"}
    except Exception as e:
        error_msg = str(e)
        if "401" in error_msg:
            error_msg = "SendGrid API Error: Check your API key."
        
        print(f"SendGrid error: {error_msg}")
        return {"status": "error", "message": error_msg}

@function_tool
def send_email(to_email: str, subject: str, html_body: str) -> Dict[str, str]:
    """Send out an email with the given subject and HTML body to the target prospect."""
    return _send_email_raw(to_email, subject, html_body)
