from prompt_optimizer.groq_client import GroqClient

class PromptOptimizer:
    def __init__(self, groq_client=None, model="mixtral-8x7b-32768"):
        if groq_client is None:
            self.groq_client = GroqClient()
        else:
            self.groq_client = groq_client
        self.model = model

    def optimize_prompt(self, user_prompt):
        """
        Optimizes a user prompt using the Groq LLM.

        Args:
            user_prompt (str): The prompt provided by the user.

        Returns:
            str: The optimized prompt.
        """
        optimization_prompt = f"""
        Rephrase and optimize the following user prompt to be more effective when working with large language models.
        Consider making it more specific, adding context, and ensuring it is clear and unambiguous.
        
        User Prompt:
        {user_prompt}
        
        Optimized Prompt:
        """
        messages = [{"role": "user", "content": optimization_prompt}]
        try:
            optimized_prompt = self.groq_client.chat_completions_create(
                model=self.model,
                messages=messages
            )
            return optimized_prompt.strip()
        except Exception as e:
            raise Exception(f"Error during prompt optimization: {e}")
