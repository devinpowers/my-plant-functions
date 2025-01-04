import logging
import azure.functions as func
from shared.email_sms import send_notification

def main(message: func.ServiceBusMessage):
    try:
        message_data = message.get_body().decode('utf-8')
        logging.info(f"Processing Service Bus message: {message_data}")

        # Parse message and send notification
        notification_data = json.loads(message_data)
        send_notification(notification_data)
        logging.info("Notification sent successfully.")

    except Exception as e:
        logging.error(f"Failed to process Service Bus message: {e}")
