from pathlib import Path
import os

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone

from llm.factory import get_embedder


from config import load_config
from observability.logger import logger


config = load_config()


class RAGIngestion:

    def __init__(self):

        self.chunk_size = config["rag"]["chunk_size"]
        self.chunk_overlap = config["rag"]["chunk_overlap"]

        self.embedding = get_embedder()

        self.pc = Pinecone(
            api_key=os.getenv("PINECONE_API_KEY"),
        )

        self.index = self.pc.Index(
            config["vector_stores"]["index_name"]
        )

        self.namespace = config["vector_stores"]["namespace"]


    async def load_document(self):

        try:

            logger.info("Loading document...")

            file_path = Path(config["vector_stores"]["data_path"])

            text = file_path.read_text(encoding="utf-8")

            logger.info("Document loaded successfully.")

            return [Document(page_content=text)]

        except Exception as ex:

            logger.exception(ex)
            raise


    async def split_documents(self, docs):

        try:

            logger.info("Chunking documents...")

            splitter = RecursiveCharacterTextSplitter(
                chunk_size=self.chunk_size,
                chunk_overlap=self.chunk_overlap
            )

            chunks = splitter.split_documents(docs)

            logger.info(f"Created {len(chunks)} chunks.")

            return chunks

        except Exception as ex:

            logger.exception(ex)
            raise


    async def ingest(self):

        try:

            docs = await self.load_document()

            chunks = await self.split_documents(docs)

            logger.info("Uploading embeddings to Pinecone...")

            PineconeVectorStore.from_documents(
                documents=chunks,
                embedding=self.embedding,
                index=self.index,
                namespace=self.namespace
            )

            logger.info("Vector DB ingestion completed.")
            return "Vector DB ingestion completed."

        except Exception as ex:

            logger.exception(ex)
            raise