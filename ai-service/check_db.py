from services.chroma_client import ChromaClient

chroma = ChromaClient()

data = chroma.collection.get()

print(data["documents"])