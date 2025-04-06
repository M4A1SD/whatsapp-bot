from pywa import WhatsApp, types
from fastapi import FastAPI
import requests
import os

class WhatsAppClient:
    # Get TARGET_SERVER with a default value if not set
    target_server = os.getenv('TARGET_SERVER', 'localhost:8002')
    
    def __init__(self, app: FastAPI, config: dict):
        """Initialize WhatsApp client with configuration."""
        self.wa = WhatsApp(
            phone_id=config['phone_id'],
            token=config['access_token'],
            server=app,
            callback_url=config['callback_url'],
            verify_token=config['verify_token'],
            app_id=config['app_id'],
            app_secret=config['app_secret'],
            webhook_challenge_delay=config['webhook_challenge_delay']
        )
        
        # Register message handlers
        self._register_handlers()
    
    def _register_handlers(self):
        """Register all message handlers."""
        @self.wa.on_message()
        def recieve_message(client: WhatsApp, msg: types.Message):
            my_phone = msg.from_user.wa_id
            self.send_message(text="Request recieved! Working on it...", to=my_phone)

            # Print debug information
            try:
                requests.post(f"http://{self.target_server}/receive_message", json={
                    "message": msg.text,
                    "phone_number": my_phone
                })
            except Exception as e:
                print(f"Error forwarding message: {str(e)}")
    
    def send_message(self, text, to):
        """Send a message to the specified number."""
        print(f"sending ${text} to ${to}")
        self.wa.send_message(
            to=to,
            text=text
        )
    
    def get_client(self):
        """Return the WhatsApp client instance."""
        return self.wa 