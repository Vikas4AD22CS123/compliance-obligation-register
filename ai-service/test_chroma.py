import chromadb

# Create client with persistent storage
client = chromadb.Client(
    chromadb.config.Settings(
        persist_directory="./chroma_data"
    )
)

# Create or get collection
collection = client.get_or_create_collection(name="compliance_docs")

# Add data (this creates embeddings automatically)
collection.add(
    documents=[
        "Company must follow environmental safety rules",
        "Financial audits must be conducted annually",
        "Employee attendance must be tracked daily"
    ],
    ids=["doc1", "doc2", "doc3"]
)

# Query similar documents
results = collection.query(
    query_texts=["environment rules"],
    n_results=2
)

print(results)