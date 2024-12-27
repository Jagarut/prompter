from groq_client import GroqClient

class PromptOptimizer:
    """
    A class for optimizing user prompts using the Groq LLM.
    """
    def __init__(self, groq_client=None, model="llama3-8b-8192", strategy="default"):
        """
        Initializes the PromptOptimizer.

        Args:
            groq_client (GroqClient, optional): An instance of GroqClient. If None, a new one is created.
            model (str, optional): The Groq model to use. Defaults to "llama3-8b-8192".
            strategy (str, optional): The optimization strategy to use. Defaults to "default".
        """
        self.groq_client = groq_client if groq_client else GroqClient()
        self.model = model
        self.strategy = strategy

    def optimize_prompt(self, user_prompt):
        """
        Optimizes a user prompt using the Groq LLM.

        Args:
            user_prompt (str): The prompt provided by the user.

        Returns:
            str: The optimized prompt.
        """
        # Define optimization prompts based on the selected strategy
        if self.strategy == "concise":
            optimization_prompt = f"""
            Rephrase the following user prompt to be more concise and to the point, while retaining all the important information.

            User Prompt:
            {user_prompt}

            Optimized Prompt:
            """
        elif self.strategy == "detailed":
            optimization_prompt = f"""
            Rephrase the following user prompt to be more detailed and explicit, adding context and ensuring it is clear and unambiguous.

            User Prompt:
            {user_prompt}

            Optimized Prompt:
            """
        else:  # default strategy
            optimization_prompt = f"""
            Rephrase and optimize the following user prompt to be more effective when working with large language models.
            Consider making it more specific, adding context, and ensuring it is clear and unambiguous. Return the optimized prompt and nothing else.

            User Prompt:
            {user_prompt}

            Optimized Prompt:
            """
        # Create a message for the Groq API
        messages = [{"role": "user", "content": optimization_prompt}]
        # Get the optimized prompt from the Groq API
        optimized_prompt = self.groq_client.chat_completions_create(
            model=self.model,
            messages=messages
        )
        # Return the optimized prompt, removing any leading/trailing whitespace
        return optimized_prompt.strip()
