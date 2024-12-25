from prompt_optimizer.groq_client import GroqClient

class PromptOptimizer:
    def __init__(self, groq_client=None, model="llama-3.3-70b-versatile", strategy="default"):
        if groq_client is None:
            self.groq_client = GroqClient()
        else:
            self.groq_client = groq_client
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
        else: # default strategy
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
