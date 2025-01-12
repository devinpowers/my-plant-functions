import os
from azure.communication.email import EmailClient

connection_string = os.getenv("ACS_CONNECTION_STRING")  # Ensure the connection string is set in environment variables




# Correctly formatted connection string

def send_test_email():
    try:
        client = EmailClient.from_connection_string(connection_string)

        message = {
            "senderAddress": "DoNotReply@b9df9d3c-fe83-444d-8ca3-7f3184c15381.azurecomm.net",  # Verified sender email
            "recipients": {
                "to": [{"address": "devinjpowers@gmail.com"}]  # Replace with recipient email
            },
            "content": {
                "subject": "Test Email",
                "plainText": "This is a plain text body.",
                "html": """
                <html>
                    <body>
                        <h1>Hello, Azure Communication Services!</h1>
                    </body>
                </html>
                """
            },
        }

        poller = client.begin_send(message)
        result = poller.result()
        print("Email sent successfully:", result)

    except Exception as ex:
        print("Failed to send test email:", ex)


# Run the test email function
send_test_email()


# Call the function to send a test email
if __name__ == "__main__":
    send_test_email()
