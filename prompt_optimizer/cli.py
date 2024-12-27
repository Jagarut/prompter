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
    parser.add_argument(
        "--model",
        type=str,
        default=DEFAULT_MODEL,
        choices=["llama3-8b-8192",
            "llama-3.3-70b-versatile",
            "llama3-groq-8b-8192-tool-use-preview",
            "llama3-70b-8192"
        ],
        help="The Groq model to use."
    )
    # Add the strategy argument
    parser.add_argument(
        "--strategy",
        type=str,
        default="default",
        choices=["default", "concise", "detailed"],
        help="The optimization strategy to use ('default', 'concise', or 'detailed')."
    )

    # Parse the arguments
    args = parser.parse_args()

    try:
        # Initialize the PromptOptimizer with the specified model and strategy
        optimizer = PromptOptimizer(model=args.model, strategy=args.strategy)
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
