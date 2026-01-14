import os
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
from typing import Dict
from agents import function_tool

def _send_email_raw(to_email: str, subject: str, html_body: str) -> Dict[str, str]:
    """Raw email sending function (for direct API calls)."""
    try:
        sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
        from_email = Email("samrude1@outlook.com")  # Verified sender
        recipient = To(to_email)
        content = Content("text/html", html_body)
        
        mail = Mail(from_email, recipient, subject, content).get()
        response = sg.client.mail.send.post(request_body=mail)
        
        print(f"SendGrid status code: {response.status_code}")
        return {"status": "success"}
    except Exception as e:
        print(f"SendGrid error: {e}")
        return {"status": "error", "message": str(e)}

@function_tool
def send_email(to_email: str, subject: str, html_body: str) -> Dict[str, str]:
    """Send out an email with the given subject and HTML body to the target prospect."""
    return _send_email_raw(to_email, subject, html_body)
