from services.groq_client import GroqClient

client = GroqClient()

response = client.generate([
    {"role": "user", "content": "Say hello"}
])

print(response)