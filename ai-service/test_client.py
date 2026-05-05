from services.groq_client import call_groq

result = call_groq("Explain compliance in simple words")
print(result)