from config import config
from observability import logger
from rag.ingestion.semantic_pinecone import RAGIngestion


def get_indexer():
   vector = config["rag"]["type"].lower()
   provider = config["vector_stores"]["provider"].lower()

   print(f"Vector: {vector}, Provider: {provider}")


   if vector == "semantic" and provider == "pinecone":
       status=RAGIngestion().ingest()
    
   return status
   
