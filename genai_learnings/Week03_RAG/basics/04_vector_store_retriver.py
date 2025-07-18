
##VECTOR STORE - BASICS
# This code demonstrates how to create a vector store using LangChain's ChromaDB and FAISS

# FAISS Vector Store
#Step 1: Load the documents/Web pages
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
doc_pdf = "resume.pdf"
loader = PyPDFLoader(doc_pdf)
pdf_documents = loader.load()

from langchain.text_splitter import RecursiveCharacterTextSplitter
recursive_text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0, 
    length_function=len
)
recursive_chunks = recursive_text_splitter.split_documents(pdf_documents)  
chunk_texts = [doc.page_content for doc in recursive_chunks]

#Step 2: Embed the documents
#from langchain.embeddings import HuggingFaceEmbeddings  
#hf_embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2") 
#hf_embedding_vector = hf_embeddings.embed_documents(chunk_texts) 

from langchain_openai import OpenAIEmbeddings
source = "Articles.pdf"  # Source document for embedding
openai_embeddings = OpenAIEmbeddings(openai_api_key="")
#openai_embedding_vector = openai_embeddings.embed_documents(chunk_texts)

#Step 3: Create the FAISS vector store
from langchain.vectorstores import FAISS     #pip install faiss-cpu
# Create a FAISS vector store from the chunk texts and embeddings
# we have to pass texts and embeddings to the FAISS vector store
faiss_vector_store = FAISS.from_texts(chunk_texts, openai_embeddings) #in one line we can create the FAISS vector store from texts and embeddings

#Step 4: retrieve documents from the FAISS vector store
retiver = faiss_vector_store.as_retriever()
query = "What is the experience he is having?"  # Example query

answers = retiver.get_relevant_documents(query)  # Retrieve relevant documents based on the query
print(f"Number of relevant documents retrieved: {len(answers)}")

for doc in answers:
    print(f"Document content: {doc.page_content}")  # Print first 500 characters of each retrieved document

