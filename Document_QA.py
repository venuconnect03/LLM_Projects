from google import genai
import os

client = genai.Client(
    api_key=os.getenv("GEN_API_KEY")
)

with open("Document_Notes.txt", "r") as file:
    document = file.read()
while True:
    question = input("Ask a question about Python: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    prompt = f"""
    Answer the question using only the document below,
    
    If the answer is not in the document,
    say: "The document does not contain this information."
    
    Explain the answer in simple English
    
    Document:
    {document}
    
    Question:
    {question}
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    print("\nAI Answer: ")
    print(response.text)