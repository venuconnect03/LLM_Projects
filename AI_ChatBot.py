from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

messages = [
    {
        "role": "system",
        "content": "You are a friendly assistant. Explain things simply"
    }
]

print("AI Chatbot is ready!")
print("Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=str(messages)
    )

    ai_replay = response.text

    print("Chatbot: ", ai_replay)

    messages.append({
        "role": "assistant",
        "content": ai_replay
    })
