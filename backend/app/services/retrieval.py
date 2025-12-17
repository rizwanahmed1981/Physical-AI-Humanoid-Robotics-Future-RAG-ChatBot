from typing import List, Dict, Any
from qdrant_client import QdrantClient
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class RetrievalService:
    def __init__(self):
        self.qdrant = QdrantClient(
            url=os.getenv("QDRANT_URL"),
            api_key=os.getenv("QDRANT_API_KEY")
        )
        self.collection_name = "physical_ai_book"

    def embed_query(self, query: str) -> List[float]:
        response = client.embeddings.create(
            model="text-embedding-3-large",
            input=query
        )
        return response.data[0].embedding

    def retrieve(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        query_vector = self.embed_query(query)

        hits = self.qdrant.search(
            collection_name=self.collection_name,
            query_vector=query_vector,
            limit=top_k
        )

        results = []
        for hit in hits:
            results.append({
                "content": hit.payload["text"],
                "source": hit.payload.get("source"),
                "chapter": hit.payload.get("chapter"),
                "section": hit.payload.get("section"),
                "score": hit.score
            })

        return results
