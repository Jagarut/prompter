import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()

# Set default values for temperature and max tokens
DEFAULT_TEMPERATURE = float(os.getenv('GROQ_DEFAULT_TEMPERATURE', 0.5))
DEFAULT_MAX_TOKENS = int(os.getenv('GROQ_DEFAULT_MAX_TOKENS', 1024))


class GroqClient:
    """
    A client for interacting with the Groq API.
    """
    def __init__(self, api_key=None):
        """
        Initializes the Groq client.

        Args:
            api_key (str, optional): The Groq API key. If None, it tries to load it from environment variables.

        Raises:
            ValueError: If no API key is provided or found in environment variables.
        """
        if api_key is None:
            api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("No Groq API key provided or found in environment variables.")
        self.client = Groq(api_key=api_key)

    def chat_completions_create(self, model, messages, temperature=DEFAULT_TEMPERATURE, max_tokens=DEFAULT_MAX_TOKENS):
        """
        Sends a chat completion request to the Groq API.

        Args:
            model (str): The name of the Groq model to use.
            messages (list): A list of message dictionaries, where each dictionary has a 'role' and 'content' key.
            temperature (float, optional): The sampling temperature. Defaults to DEFAULT_TEMPERATURE.
            max_tokens (int, optional): The maximum number of tokens to generate. Defaults to DEFAULT_MAX_TOKENS.

        Returns:
            str: The content of the generated message.
        """
        chat_completion = self.client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )
        return chat_completion.choices[0].message.content
