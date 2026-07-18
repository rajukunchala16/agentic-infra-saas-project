import os

from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone

from llm.factory import get_embedder

from config import load_config
from observability.logger import logger


config = load_config()


class RAGRetriever:

    def __init__(self):

        self.embedding = get_embedder()

        self.pc = Pinecone(
            api_key=os.getenv("PINECONE_API_KEY")
        )

        self.index = self.pc.Index(
            config["vector_stores"]["index_name"]
        )

        self.namespace = config["vector_stores"]["namespace"]

        self.vectorstore = PineconeVectorStore(
            index=self.index,
            embedding=self.embedding,
            namespace=self.namespace
        )


    async def retrieve(
        self,
        query: str,
        k: int = 4
    ):

        try:

            logger.info(
                f"Searching Pinecone. Query={query}, K={k}"
            )

            docs = self.vectorstore.similarity_search(
                query=query,
                k=k
            )

            logger.info(
                f"Retrieved {len(docs)} documents."
            )

            return docs

        except Exception as ex:

            logger.exception(ex)
            raise