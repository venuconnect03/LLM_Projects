from google import genai
import os
import numpy as np

client = genai.Client(
    api_key=os.getenv("GEN_API_KEY")
)

with open("AI_Knowledge_Notes.txt", "r", encoding="utf-8") as file:
    document = file.read()

chunks = [
    chunk.strip()
    for chunk in document.split("\n\n")
    if chunk.strip()
]

print("Document loaded successfully!")
print("Number of chunks: ", len(chunks))

chunk_embeddings = []

for chunk in chunks:
    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=chunk
    )

    embedding = response.embeddings[0].values

    chunk_embeddings.append(embedding)

while True:
    question = input("\nAsk a question:")

    if question == "exit":
        print("See you again!")
        break

    query_response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=question
    )

    query_embedding = query_response.embeddings[0].values

    similarity_scores = []

    for embedding in chunk_embeddings:
        score = np.dot(embedding, query_embedding) / (
            np.linalg.norm(query_embedding)
            * np.linalg.norm(embedding)
        )

        similarity_scores.append(score)

    top_indices = np.argsort(similarity_scores)[::-1][:2]

    relevant_chunks = [
        chunks[index]
        for index in top_indices
    ]

    context = "\n\n".join(relevant_chunks)

    prompt = f"""
    You are a helpful AI knowledge assistant.
    
    Answer the question using only the provided context.
    
    If the context does not contain the answer,
    say that the information was not found in the document.
    
    Explain the answer in simple English.
    
    Context:
    {context}
    
    Question:
    {question}
    
    Answer:
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    print("\nRelevant information")
    print(context)

    print("\n AI Answer")
    print(response.text)

