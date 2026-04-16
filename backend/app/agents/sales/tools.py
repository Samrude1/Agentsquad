import os
import resend
# from sendgrid.helpers.mail import Mail, Email, To, Content
from typing import Dict
from agents import function_tool

def _send_email_raw(to_email: str, subject: str, html_body: str) -> Dict[str, str]:
    """Raw email sending function (for direct API calls)."""
    try:
        resend.api_key = os.environ.get('RESEND_API_KEY')
        
        # Use onboarding address for demo
        from_email = "Agent Squad <onboarding@resend.dev>"
        
        response = resend.Emails.send({
            "from": from_email,
            "to": [to_email],
            "subject": subject,
            "html": html_body
        })
        
        print(f"Resend success: {response}")
        return {"status": "success"}
    except Exception as e:
        error_msg = str(e)
        if "401" in error_msg:
            error_msg = "Resend API Error: Check your API key."
        
        print(f"Resend error: {error_msg}")
        return {"status": "error", "message": error_msg}

@function_tool
def send_email(to_email: str, subject: str, html_body: str) -> Dict[str, str]:
    """Send out an email with the given subject and HTML body to the target prospect."""
    return _send_email_raw(to_email, subject, html_body)
