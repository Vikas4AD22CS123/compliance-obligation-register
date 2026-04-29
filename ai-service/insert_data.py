from services.chroma_client import ChromaClient
import uuid

chroma = ChromaClient()

texts = [
    "Tax rules are regulations that companies must follow",
    "Safety rules are guidelines that ensure employee safety at the workplace",
    "Data protection is the process of safeguarding personal information from misuse",
    "Labor laws are regulations that govern employee rights and working conditions",
    "Audit requirements are rules that ensure companies regularly review financial records"
]

for text in texts:
    chroma.add_text(text, str(uuid.uuid4()))

print("Data inserted successfully")