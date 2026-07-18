from langchain.tools import tool


from rag.retriever.factory import get_retriever
from observability import logger





@tool
def search_logs(query: str) -> str:
   """
   Search the logs for relevant information.
   Use this tool whenever you need to find log entries related to a question.
   """
   logger.info(f"Tool called: search_logs with query: {query}")
   retrieve = get_retriever()
   chunks = retrieve(query, k=5)
   if not chunks:
       return "No relevant log entries found."


   results = []
   for chunk in chunks:
       results.append(
           f"File: {chunk['source']} (lines {chunk['start_line']}-{chunk['end_line']})\n"
           f"Type: {chunk['type']} — {chunk['name']}\n"
           f"Code:\n{chunk['content']}\n"
       )
   return "\n---\n".join(results)