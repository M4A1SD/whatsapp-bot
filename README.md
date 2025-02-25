# WhatsApp Bot

A WhatsApp bot application built with FastAPI and pywa wrapper.

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   maybe pip install -e .?
   ```
3. Set up your environment variables in a `.env` file like in the example:
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

## Using the API with Python Requests

You can use the Python `requests` library to send messages to your WhatsApp bot API. Here's an example:

 see the `send_message_example.py` file.

A shell script example is available in `curl_example.sh`. 

##

make sure your 2 apps are on the same python envirment
use ```pip install -e .```
and then import the app like this 
functionalities available : 







if you wanna use this as it is, not like a package in another app, then run the standalone file.