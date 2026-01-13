import os
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
from typing import Dict
from agents import function_tool

@function_tool
def send_email(body: str):
    """ Send out an email with the given body to all sales prospects """
    try:
        sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
        from_email = Email("samrude1@outlook.com") # Verified sender
        to_email = To("srautanen77@gmail.com")     # Recipient
        content = Content("text/plain", body)
        mail = Mail(from_email, to_email, "Sales email", content).get()
        response = sg.client.mail.send.post(request_body=mail)
        print(f"SendGrid status code: {response.status_code}")
        return {"status": "success"}
    except Exception as e:
        print(f"SendGrid error: {e}")
        return {"status": "error", "message": str(e)}

@function_tool
def send_html_email(subject: str, html_body: str) -> Dict[str, str]:
    """ Send out an email with the given subject and HTML body to all sales prospects """
    try:
        sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
        from_email = Email("samrude1@outlook.com") # Verified sender
        to_email = To("srautanen77@gmail.com")     # Recipient
        content = Content("text/html", html_body)
        mail = Mail(from_email, to_email, subject, content).get()
        response = sg.client.mail.send.post(request_body=mail)
        print(f"SendGrid HTML status code: {response.status_code}")
        return {"status": "success"}
    except Exception as e:
        print(f"SendGrid HTML error: {e}")
        return {"status": "error", "message": str(e)}
