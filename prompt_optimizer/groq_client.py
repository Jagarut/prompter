import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

DEFAULT_TEMPERATURE = float(os.getenv('GROQ_DEFAULT_TEMPERATURE', 0.5))
DEFAULT_MAX_TOKENS = int(os.getenv('GROQ_DEFAULT_MAX_TOKENS', 1024))


class GroqClient:
    def __init__(self, api_key=None):
        if api_key is None:
            api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("No Groq API key provided or found in environment variables.")
        self.client = Groq(api_key=api_key)

    def chat_completions_create(self, model, messages, temperature=DEFAULT_TEMPERATURE, max_tokens=DEFAULT_MAX_TOKENS):
        """
        Send a chat completion request to the Groq API.

        Args:
            model (str): The name of the Groq model to use.
            messages (list): A list of message dictionaries, where each dictionary has a 'role' and 'content' key.
            temperature (float, optional): The sampling temperature. Defaults to 0.5.
            max_tokens (int, optional): The maximum number of tokens to generate. Defaults to 1024.

        Returns:
            str: The content of the generated message.

        Raises:
            Exception: If there is an error during the API request.
        """
        chat_completion = self.client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )
        return chat_completion.choices[0].message.content
