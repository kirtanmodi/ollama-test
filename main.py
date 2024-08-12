import ollama

# Get user input from terminal
user_input = input("Enter your question: ")

stream = ollama.chat(
    model="llama3.1:8b-instruct-q8_0",
    stream=True,
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": user_input
        }
    ]
)

# for direct response
# for key, value in stream.items():
#     if key == "message":
#         print(value['content'])

# for streaming response
for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
