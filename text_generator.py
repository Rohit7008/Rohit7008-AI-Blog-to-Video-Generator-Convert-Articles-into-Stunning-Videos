import openai
from api_key import API_KEY  # Ensure your API key is correctly imported

openai.api_key = API_KEY

# Set the model to use
model_engine = "gpt-3.5-turbo"  # Updated to the latest model

# Get user input
text = input("What topic do you want to write about? ")

print("The AI BOT is trying now to generate a new text for you...")

# Generate text using OpenAI's new API format
response = openai.ChatCompletion.create(
    model=model_engine,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Write about {text}."}
    ],
    max_tokens=1024,
    temperature=0.5
)

# Extract generated text
generated_text = response["choices"][0]["message"]["content"]

# Save the text in a file
with open("generated_text.txt", "w", encoding="utf-8") as file:
    file.write(generated_text.strip())

print("The Text Has Been Generated Successfully!")
print("The generated text is:")
print(generated_text.strip())
# The generated text is saved in 'generated_text.txt'
