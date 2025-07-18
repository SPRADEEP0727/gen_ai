## EMBEDINGS FOR RAG - BASICS ##
# pip install langchain langchain openai sentence-transformers
# This code demonstrates how to create embeddings for text using LangChain's OpenAIEmbeddings and SentenceTransformerEmbeddings.

from langchain_openai import OpenAIEmbeddings
source = "Articles.pdf"  # Source document for embedding
openai_embeddings = OpenAIEmbeddings(openai_api_key="")  # Replace with your OpenAI API key 

openai_embedding_vector = openai_embeddings.embed_query("Hello, how are you?")  # Create an embedding for a sample text
#print(f"OpenAI Embedding Vector: {openai_embedding_vector}") # Print the embedding vector


#With Hugginface embeddings
from langchain.embeddings import HuggingFaceEmbeddings
hf_embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")  # Load a pre-trained model from HuggingFace
hf_embedding_vector = hf_embeddings.embed_query("Hello, how are you?")  # Create an embedding for a sample text
print(f"HuggingFace Embedding Vector: {hf_embedding_vector}")

