from pywa import WhatsApp, types
from fastapi import FastAPI

class WhatsAppClient:
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
        def hello(client: WhatsApp, msg: types.Message):
            self.send_message(f"Hello {msg.from_user.name}!")
    
    def send_message(self, text, to="+972543557471"):
        """Send a message to the specified number."""
        self.wa.send_message(
            to=to,
            text=text
        )
    
    def get_client(self):
        """Return the WhatsApp client instance."""
        return self.wa 