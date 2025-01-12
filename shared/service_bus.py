import os
from azure.servicebus import ServiceBusClient, ServiceBusMessage
import json
import logging

def send_message_to_service_bus(message_payload):
    try:
        # Fetch connection details from environment variables
        connection_string = os.getenv("SERVICE_BUS_CONNECTION_STRING")
        queue_name = os.getenv("SERVICE_BUS_QUEUE_NAME", "RemindersQueue")

        if not connection_string or not queue_name:
            raise ValueError("Missing Service Bus connection string or queue name")

        # Connect to the Service Bus
        with ServiceBusClient.from_connection_string(connection_string) as client:
            # Get sender for the queue
            sender = client.get_queue_sender(queue_name)
            with sender:
                # Send message as JSON
                message = ServiceBusMessage(json.dumps(message_payload))
                sender.send_messages(message)
                logging.info(f"Message sent to Service Bus queue: {queue_name}")
    except Exception as e:
        logging.error(f"Failed to send message to Service Bus: {e}")
        raise
