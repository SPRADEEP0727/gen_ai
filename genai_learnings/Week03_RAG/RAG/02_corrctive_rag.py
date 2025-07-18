
##SELF RAG - Self Retrieval Augmented Generation
# This code demonstrates how to load a PDF document, split it into chunks, create embeddings,

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS 
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
import os

doc_pdf = "../basics/resume.pdf"
loader = PyPDFLoader(doc_pdf)
pdf_documents = loader.load()

from langchain.text_splitter import RecursiveCharacterTextSplitter
recursive_text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=100, 
    length_function=len
)
recursive_chunks = recursive_text_splitter.split_documents(pdf_documents)  
chunk_texts = [doc.page_content for doc in recursive_chunks]



source = "Articles.pdf"  # Source document for embedding
#openai_embeddings = OpenAIEmbeddings()
#openai_embedding_vector = openai_embeddings.embed_documents(chunk_texts)


from langchain.vectorstores import FAISS    
faiss_vector_store = FAISS.from_texts(chunk_texts, openai_embeddings) 


retriever = faiss_vector_store.as_retriever()
llm = ChatOpenAI(temperature=0.0, model_name="gpt-4o-mini")

qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

def corrective_rag(query):
    first_guess = llm.invoke(f"Q: {query}\nA:")

    correction = qa.run(query)
    return f"original guess: {first_guess.content}\n\ncorrected answer: {correction}"
    #give to LLm and get the final answer


print(corrective_rag("tell about pradeep"))  # Example query

#NOTE: this method used to correct the answer from the LLM if it is not confident enough.
#This is useful for scenarios where we want to avoid unnecessary retrieval calls and only use them when the LLM is not confident in its answer.
#This can help in reducing the number of API calls and improving the performance of the application.


