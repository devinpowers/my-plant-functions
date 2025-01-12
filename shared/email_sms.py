import logging
from azure.communication.email import EmailClient
import os

def send_notification(data):
    """
    Dispatches the notification based on the reminder type (email or SMS).
    Currently, only email notifications are supported.
    """
    if data["reminder_type"] == "email":
        send_email(data)
    else:
        logging.error(f"Unsupported reminder type: {data['reminder_type']}")


def send_email(data):
    """
    Sends an email notification using Azure Communication Services.
    """
    connection_string = os.getenv("ACS_CONNECTION_STRING")

    if not connection_string:
        logging.error("Azure Communication Services connection string not found.")
        return

    try:
        client = EmailClient.from_connection_string(connection_string)
        message = {
            "senderAddress": "DoNotReply@b9df9d3c-fe83-444d-8ca3-7f3184c15381.azurecomm.net",
            "recipients": {
                "to": [{"address": data["user_contact"]}]
            },
            "content": {
                "subject": "Plant Watering Reminder",
                "plainText": "Time to water your plant!",
                "html": f"""
                <html>
                    <body>
                        <h1>Reminder to Water Your Plant!</h1>
                        <p>{data["message"]}</p>
                        <img src="{data.get('plant_photo_url', '')}" alt="Plant Photo" style="max-width: 300px;">
                    </body>
                </html>
                """
            },
        }

        poller = client.begin_send(message)
        result = poller.result()
        logging.info(f"Email sent successfully. Message ID: {result.get('message_id', 'unknown')}")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")
