import requests
import json

def send_whatsapp_message(phone_number, message):
    """
    Send a WhatsApp message using the API.
    
    Args:
        phone_number (str): The recipient's phone number with country code (e.g., "+1234567890")
        message (str): The message text to send
        
    Returns:
        dict: The API response
    """
    # API endpoint URL - update with your actual server address
    url = "http://localhost:8000/send-whatsapp-message"
    
    # Request headers
    headers = {
        "Content-Type": "application/json"
    }
    
    # Request payload
    payload = {
        "phone_number": phone_number,
        "message": message
    }
    
    # Send the POST request
    response = requests.post(
        url=url,
        headers=headers,
        data=json.dumps(payload)
    )
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

if __name__ == "__main__":
    # Example usage
    recipient = "+1234567890"  # Replace with the actual phone number
    message_text = "Hello from the WhatsApp API!"
    
    result = send_whatsapp_message(recipient, message_text)
    
    if result:
        print("Message sent successfully!")
        print(f"Response: {result}") 