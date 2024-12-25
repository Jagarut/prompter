import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

class GroqClient:
    def __init__(self, api_key=None):
        if api_key is None:
            api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("No Groq API key provided or found in environment variables.")
        self.client = Groq(api_key=api_key)

    def chat_completions_create(self, model, messages, temperature=1.0, top_p=1.0, max_tokens=None):
        """
        Send a chat completion request to the Groq API.

        Args:
            model (str): The name of the Groq model to use.
            messages (list): A list of message dictionaries, where each dictionary has a 'role' and 'content' key.
            temperature (float, optional): The sampling temperature. Defaults to 1.0.
            top_p (float, optional): The nucleus sampling probability. Defaults to 1.0.
            max_tokens (int, optional): The maximum number of tokens to generate. Defaults to None.

        Returns:
            str: The content of the generated message.

        Raises:
            Exception: If there is an error during the API request.
        """
        try:
            chat_completion = self.client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                top_p=top_p,
                max_tokens=max_tokens
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            raise Exception(f"Error during Groq API request: {e}")
