from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="openai-community/gpt2"
)

prompt = input("Enter a sentence: ")

result = generator(
    prompt,
    max_new_tokens=50,
    do_sample=True,
    temperature=0.7,
    pad_token_id=50256
)

print("\nGenerated Text: ")
print(result[0],["generated_text"])