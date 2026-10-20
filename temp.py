from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="distilgpt2"
)

prompt = "The beauty of nature is"

print("\n--- Low Temperature ---")
result = generator(
    prompt,
    max_new_tokens=30,
    do_sample=True,
    temperature=0.2
)
print(result[0]["generated_text"])


print("\n--- High Temperature ---")
result = generator(
    prompt,
    max_new_tokens=30,
    do_sample=True,
    temperature=1.2
)
print(result[0]["generated_text"])


print("\n--- Top-K = 5 ---")
result = generator(
    prompt,
    max_new_tokens=30,
    do_sample=True,
    top_k=5
)
print(result[0]["generated_text"])


print("\n--- Top-P = 0.8 ---")
result = generator(
    prompt,
    max_new_tokens=30,
    do_sample=True,
    top_p=0.8
)
print(result[0]["generated_text"])