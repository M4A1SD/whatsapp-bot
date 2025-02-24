from pywa import WhatsApp, filters, types
from pywa.types import Message
from dotenv import load_dotenv
import os



from fastapi import FastAPI

# Create a FastAPI app
fastapi_app = FastAPI()





# Clear existing environment variables to avoid caching (optional, for testing)
for key in ['PHONE_NUMBER_ID_WA', 'ACCESS_TOKEN_WA', 'APP_ID_WA', 'APP_SECRET_WA']:
    os.environ.pop(key, None)

# Load environment variables fresh each run
load_dotenv(override=True)  # Force override of existing env vars

phone_id = os.getenv('PHONE_NUMBER_ID_WA')
access_token = os.getenv('ACCESS_TOKEN_WA')
app_id = os.getenv('APP_ID_WA')
app_secret = os.getenv('APP_SECRET_WA')

# Add debug prints to verify environment variables
print("Checking environment variables:")
print(access_token)

wa = WhatsApp(
    phone_id=phone_id,
    token=access_token,
    server=fastapi_app,
    callback_url="https://5930-5-29-244-156.ngrok-free.app",  # Replace with your public HTTPS URL
    verify_token="rito",  # Use a more secure token
    app_id=app_id,
    app_secret=app_secret,
    webhook_challenge_delay=20  # Add delay to handle slow connections
)

def send_message(text):
    wa.send_message(
        to="+972543557471",
        text=text
    )


@wa.on_message()
def hello(client: WhatsApp, msg: types.Message):
    # msg.react("👋")  # React with a waving hand emoji
    send_message(f"Hello {msg.from_user.name}!")

# Handler for incoming text messages
# @wa.on_message()
# def handle_message(client: WhatsApp, msg: Message):
#     print(f"Received message from {msg.from_user.wa_id}: {msg.text}")
    
#     # React to "hello" with a reply
#     if msg.text.lower() == "hello":
#         client.send_message(
#             to=msg.from_user.wa_id,
#             text="Hi there! You said hello!"
#         )
#         print(f"Replied to {msg.from_user.wa_id}")

    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(fastapi_app, host="localhost", port=8000)
