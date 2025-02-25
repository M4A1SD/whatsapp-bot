# WhatsApp Bot

A WhatsApp bot application built with FastAPI and pywa.

## Setup

1. Make sure you have Python 3.7+ installed
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up your environment variables in a `.env` file:
   ```
   PHONE_NUMBER_ID_WA=your_phone_id
   ACCESS_TOKEN_WA=your_access_token
   APP_ID_WA=your_app_id
   APP_SECRET_WA=your_app_secret
   CALLBACK_URL=your_ngrok_url
   ```
4. Make sure your ngrok URL is up-to-date in the `.env` file

## Running the Application

There are two ways to run the application:

### Option 1: Using the run script (recommended)

```
python run.py
```

### Option 2: Running directly from the module

```
cd whatsappModule
python main.py
```

## API Endpoints

- `POST /send-whatsapp-message`: Send a WhatsApp message
  - Request body:
    ```json
    {
      "phone_number": "+1234567890",
      "message": "Hello, world!"
    }
    ``` 