from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from whatsapp_client import WhatsAppClient

class SendMessageRequest(BaseModel):
    phone_number: str
    message: str

def setup_routes(app: FastAPI, whatsapp_client: WhatsAppClient):
    """Set up API routes for the FastAPI application."""
    
    @app.post("/send-whatsapp-message")
    async def send_whatsapp_message(request: SendMessageRequest):
        try:
            # Send the message using the WhatsApp client
            whatsapp_client.send_message(
                text=request.message,
                to=request.phone_number
            )
            return {"status": "success", "message": f"Message sent to {request.phone_number}"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to send message: {str(e)}") 