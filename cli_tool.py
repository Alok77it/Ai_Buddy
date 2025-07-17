from gemini_utils import ask_gemini

print("🤖 AI Code Buddy (CLI) – Type 'exit' to quit.\n")

while True:
    user_input = input("🧑‍💻 You: ")
    if user_input.lower() == "exit":
        break
    response = ask_gemini(user_input)
    print("🤖 Gemini:", response)

