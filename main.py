# First install Twilio with:
# pip install twilio

from twilio.rest import Client

# Your Twilio credentials from https://www.twilio.com/console
account_sid = "your_account_sid"
auth_token = "your_auth_token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello, this is a test SMS from Python!",
    from_="+1234567890",  # Your Twilio number
    to="+919876543210"    # Receiver's phone number
)

print("Message sent! SID:", message.sid)

