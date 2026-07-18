from config import config
from observability import logger




def get_retriever():
   vector = config["rag"]["type"].lower()
   provider = config["vector_stores"]["provider"].lower()


   if vector == "semantic" and provider == "pinecone":
       from .semantic_rag import RAGRetriever
   


   return RAGRetriever()