import os
from azure.servicebus import ServiceBusClient, ServiceBusMessage
import json

def send_message_to_service_bus(message_payload):
    connection_string = os.getenv("SERVICE_BUS_CONNECTION_STRING")
    queue_name = os.getenv("SERVICE_BUS_QUEUE_NAME", "RemindersQueue")

    with ServiceBusClient.from_connection_string(connection_string) as client:
        sender = client.get_queue_sender(queue_name)
        message = ServiceBusMessage(json.dumps(message_payload))
        sender.send_messages(message)
