"""
WhatsApp Bot Module

This package contains modules for setting up and running a WhatsApp bot
with FastAPI integration.
"""


from .config import load_config
from .whatsapp_client import WhatsAppClient
from .api import setup_routes, SendMessageRequest
from .main import start_app


__version__ = "0.1.6" 