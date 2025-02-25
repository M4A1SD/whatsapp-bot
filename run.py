"""
Run script for WhatsApp Bot application.
This script properly imports and runs the WhatsApp Bot application.
"""

import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the app from the whatsappModule
from whatsappModule.main import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000) 