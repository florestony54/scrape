from twilio.rest import Client
from items import item_update, airpods


# ** is filler text; enter actual phone numbers, token, and sid
account_sid = [Twilio account sid]**
auth_token = [Twilio auth token]**
client = Client(account_sid, auth_token)

if airpods.status == "IN STOCK":
    message = client.messages.create(
                                body=item_update,
                                from_=[Twilio Number]**,
                                to=[Recipient Number]**
    )
    print(message.sid)
else:
    print("OUT OF STOCK")
