from fastapi import FastAPI
import uvicorn

from .config import load_config
from .whatsapp_client import WhatsAppClient
from .api import setup_routes

# Create a FastAPI app
fastapi_app = FastAPI()

# external app creates config based on indevidual needs. and passes it to this package.
def main(config: dict):

    # Initialize WhatsApp client
    whatsapp_client = WhatsAppClient(fastapi_app, config)
    
    # Set up API routes
    setup_routes(fastapi_app, whatsapp_client)

    return fastapi_app

# Create the application instance
def start_app(config: dict):
    app = main(config)
    return app

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
