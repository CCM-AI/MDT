# MDT AI Assistant

This project is a simple AI assistant for a multidisciplinary team (MDT) that answers patient questions using a Flask web application.

## How to Use

1. Send a POST request to the `/ask` endpoint with a JSON body containing the question.
2. Example:
   ```json
   {
       "question": "What is your name?"
   }
