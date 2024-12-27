import os
import argparse
from prompt_optimizer import PromptOptimizer
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the default model from environment variables
DEFAULT_MODEL = os.getenv('GROQ_DEFAULT_MODEL')

def main():
    """
    Main function to parse command line arguments and optimize user prompts.
    """
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Optimize user prompts using Groq LLM.")
    # Add the prompt argument
    parser.add_argument("prompt", type=str, help="The prompt to optimize.")
    # Add the model argument
    parser.add_argument("--model", type=str, default=DEFAULT_MODEL, help="The Groq model to use.")

    # Parse the arguments
    args = parser.parse_args()

    try:
        # Initialize the PromptOptimizer with the specified model
        optimizer = PromptOptimizer(model=args.model)
        # Optimize the prompt
        optimized_prompt = optimizer.optimize_prompt(args.prompt)
        # Print the optimized prompt
        print("Optimized Prompt:")
        print(optimized_prompt)
    except Exception as e:
        # Print any errors that occur
        print(f"Error: {e}")

if __name__ == "__main__":
    # Execute the main function
    main()
