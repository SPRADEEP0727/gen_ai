
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

def self_rag(query):
    print("First attempt without retrieval:")
    first_answer = llm.invoke(f"Q: {query}\nA:")
    first_answer_text = first_answer.content

    if "I'm not sure" in first_answer_text or "I don't know" in first_answer_text or "there is no information" in first_answer_text or len(first_answer_text) < 30:
        print("Low confidence in the first answer, using retrieval:")
        improved_answer = qa.run(query)
        return improved_answer
    else:
        print("High confidence in the first answer, no retrieval needed.")
        return first_answer_text
    

responce = self_rag("what is his work experience?")  # Example query
print(responce)

#NOTE: Mainly for Q & A we can use this self RAG approach, where we can first try to get the answer from the LLM and if it is not confident enough then we can use the retriever to get the answer.
#This is useful for scenarios where we want to avoid unnecessary retrieval calls and only use them when the LLM is not confident in its answer.
#This can help in reducing the number of API calls and improving the performance of the application.
# for resume analysis - we have to use with retriver, otherwise it will not work as expected.
#This is a simple example of how to use self RAG with LangChain and OpenAI 


