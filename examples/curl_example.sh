#!/bin/bash
# Example of sending a WhatsApp message using curl

# Replace with the actual phone number
PHONE_NUMBER="+1234567890"
MESSAGE="Hello from curl!"

# Send the POST request
curl -X POST "http://localhost:8000/send-whatsapp-message" \
  -H "Content-Type: application/json" \
  -d "{\"phone_number\":\"$PHONE_NUMBER\",\"message\":\"$MESSAGE\"}"

# Add a newline at the end for better formatting
echo 