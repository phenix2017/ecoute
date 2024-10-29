import openai
from keys import OPENAI_API_KEY  # Import the API key from keys.py

# Initialize the OpenAI API key
openai.api_key = OPENAI_API_KEY

# List all available models
def list_available_models():
    models = openai.Model.list()
    for model in models['data']:
        print(model['id'])

# Call the function to display available models
if __name__ == "__main__":
    list_available_models()
