import logging
import azure.functions as func
from datetime import datetime
from shared.database import get_due_plants
from shared.service_bus import send_message_to_service_bus

def main(timer: func.TimerRequest) -> None:
    logging.info('CheckSchedule Function triggered at: %s', datetime.utcnow())

    try:
        # Query database for plants needing reminders
        due_plants = get_due_plants()
        logging.info(f"Found {len(due_plants)} plants needing reminders.")
    except Exception as e:
        logging.error(f"Database query failed: {e}")
        return

    # Send reminders to Service Bus Queue
    for plant in due_plants:
        message_payload = {
            "plant_id": plant["id"],
            "plant_name": plant["name"],
            "user_contact": plant["contact_email"],
            "reminder_type": "email",  # or "sms"
            "message": f"Time to water your plant '{plant['name']}'!"
        }
        try:
            send_message_to_service_bus(message_payload)
            logging.info(f"Reminder sent for plant {plant['name']}")
        except Exception as e:
            logging.error(f"Failed to send reminder for plant {plant['id']}: {e}")
