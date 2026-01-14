import os
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
from typing import Dict
from agents import function_tool

@function_tool
def send_email(to_email: str, subject: str, html_body: str) -> Dict[str, str]:
    """ Send out an email with the given subject and HTML body to the target prospect """
    try:
        sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
        from_email = Email("samrude1@outlook.com") # Verified sender
        recipient = To(to_email)                   # Dynamic Recipient
        content = Content("text/html", html_body)
        
        mail = Mail(from_email, recipient, subject, content).get()
        response = sg.client.mail.send.post(request_body=mail)
        
        print(f"SendGrid status code: {response.status_code}")
        return {"status": "success"}
    except Exception as e:
        print(f"SendGrid error: {e}")
        return {"status": "error", "message": str(e)}

@function_tool
def return_draft(to_email: str, subject: str, html_body: str) -> Dict[str, str]:
    """ Submit the final email draft for human review. Do not send it yet. """
    return {
        "status": "draft_created",
        "to_email": to_email,
        "subject": subject,
        "html_body": html_body
    }
