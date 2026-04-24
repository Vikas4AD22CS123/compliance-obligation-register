import chromadb

class ChromaClient:
    def __init__(self):
        self.client = chromadb.PersistentClient(path="./chroma_data")

        self.collection = self.client.get_or_create_collection(
            name="compliance_docs"
        )

    def add_text(self, text, id):
        self.collection.add(
            documents=[text],
            ids=[id]
        )

    def query(self, query_text):
        results = self.collection.query(
            query_texts=query_text,
            n_results=3
        )
        return results