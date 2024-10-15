import os
import openai

# Set the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Create a completion
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="who is Rohit Sharma",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

# Print the response
print(response.choices[0].text.strip())
