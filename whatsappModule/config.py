from dotenv import load_dotenv
import os

def load_config():
    """Load environment variables and return configuration."""
    # Clear existing environment variables to avoid caching (optional, for testing)
    for key in ['PHONE_NUMBER_ID_WA', 'ACCESS_TOKEN_WA', 'APP_ID_WA', 'APP_SECRET_WA']:
        os.environ.pop(key, None)

    # Load environment variables fresh each run
    load_dotenv(override=True)  # Force override of existing env vars

    print("make sure ngrok updated")
    print("current ngrok url: ", os.getenv('CALLBACK_URL'))

    config = {
        'phone_id': os.getenv('PHONE_NUMBER_ID_WA'),
        'access_token': os.getenv('ACCESS_TOKEN_WA'),
        'app_id': os.getenv('APP_ID_WA'),
        'app_secret': os.getenv('APP_SECRET_WA'),
        'callback_url': os.getenv('CALLBACK_URL'),  # Replace with your public HTTPS URL
        'verify_token': "rito",  # Use a more secure token
        'webhook_challenge_delay': 20  # Add delay to handle slow connections
    }

    # Debug print to verify environment variables


    return config 