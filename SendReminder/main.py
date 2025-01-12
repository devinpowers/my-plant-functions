import logging
import azure.functions as func
from shared.email_sms import send_notification
import json

def main(message: func.ServiceBusMessage):
    """
    Function triggered by Azure Service Bus messages to send notifications.
    """
    try:
        # Decode and parse the message
        message_data = message.get_body().decode('utf-8')
        logging.info(f"Processing Service Bus message: {message_data}")

        # Convert message to JSON
        notification_data = json.loads(message_data)

        # Send the notification (email)
        send_notification(notification_data)
        logging.info("Notification sent successfully.")
    except Exception as e:
        logging.error(f"Failed to process Service Bus message: {e}")
