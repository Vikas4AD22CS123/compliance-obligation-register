from services.chroma_client import ChromaClient

client = ChromaClient()

# Add data
client.add_text("Company must follow tax regulations", "1")

# Query
result = client.query("tax rules")

print(result)