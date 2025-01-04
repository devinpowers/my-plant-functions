import logging
import sendgrid
from sendgrid.helpers.mail import Mail

def send_notification(data):
    if data["reminder_type"] == "email":
        send_email(data)
    elif data["reminder_type"] == "sms":
        send_sms(data)

def send_email(data):
    sg = sendgrid.SendGridAPIClient(api_key=os.getenv("SENDGRID_API_KEY"))
    message = Mail(
        from_email="your-email@example.com",
        to_emails=data["user_contact"],
        subject="Plant Watering Reminder",
        html_content=data["message"]
    )
    try:
        response = sg.send(message)
        logging.info(f"Email sent: {response.status_code}")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")

def send_sms(data):
    logging.warning("SMS functionality not implemented yet.")
