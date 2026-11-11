from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="openai-community/gpt2"
)

while True:
    prompt = input("Enter a sentence: ")

    if prompt.lower() == "exit":
        print("\nSee you later!")
        break

    result = generator(
        prompt,
        max_new_tokens=50,
        do_sample=True,
        temperature=0.7,
        pad_token_id=50256
    )

    print("\nGenerated Text: ")
    print(result[0],["generated_text"])