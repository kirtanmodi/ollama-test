import ollama
import os
from dotenv import load_dotenv

load_dotenv()


def chat():
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        }
    ]

    while True:
        user_input = input("\nEnter your question (or 'exit' to quit): ")

        if user_input.lower() == 'exit':
            break

        messages.append({"role": "user", "content": user_input})

        stream = ollama.chat(
            model=os.getenv('OLLAMA_MODEL'),
            stream=True,
            messages=messages
        )

        print("\nAssistant: ", end='', flush=True)
        for chunk in stream:
            print(chunk['message']['content'], end='', flush=True)

        messages.append(
            {"role": "assistant", "content": chunk['message']['content']})

    print("\nGoodbye!")


if __name__ == "__main__":
    chat()
