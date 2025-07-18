##### DATA INGESTION AND RETRIEVAL AUGMENTED GENERATION (RAG) - BASICS #####
# This code demonstrates how to load various types of documents using LangChain's document loaders.

#Text file loader for LangChain
from langchain_community.document_loaders import TextLoader

Text_file = "test.txt"
loader = TextLoader(Text_file, encoding="utf-8")
documents = loader.load()

#print(f"Number of documents loaded: {len(documents)}")
#print(f"First document content: {documents[0].page_content}")
#-----------------------------------------------------------------------------------------------------
#PDF file loader for LangChain
from langchain_community.document_loaders import PyPDFLoader
PDF_file = "Articles.pdf"
loader = PyPDFLoader(PDF_file)
pdf_ocuments = loader.load()

#print(f"Number of PDF documents loaded: {len(pdf_ocuments)}")
#print(f"First PDF document content: {pdf_ocuments[0].page_content[:500]}")  # Print first 500 characters of the first PDF document

#-----------------------------------------------------------------------------------------------------
#web page loader for LangChain
from langchain_community.document_loaders import WebBaseLoader  #pip install bs4 - for BeautifulSoup - web scraping
web_page_url = "https://www.wikipedia.org/"
loader = WebBaseLoader(web_page_url)
web_documents = loader.load()
#print(f"Number of web documents loaded: {len(web_documents)}")

#------------------------------------------------------------------------------------------------------
#Arxiv loader for LangChain
from langchain_community.document_loaders import ArxivLoader #pip install arxiv 
arxiv_url = "2507.12452"  # Example Arxiv number - pip install pymupdf to use arxiv number
#arxiv_url = "https://arxiv.org/abs/2507.12452"  # Alternatively, you can use the full URL
loader = ArxivLoader(arxiv_url)
arxiv_documents = loader.load() 
#print(f"Number of Arxiv documents loaded: {len(arxiv_documents)}")
#print(f"First Arxiv document content: {arxiv_documents[0].page_content[:500]}")  # Print first 500 characters of the first Arxiv document

#------------------------------------------------------------------------------------------------------
#wikipedia loader for LangChain
from langchain_community.document_loaders import WikipediaLoader  #pip install wikipedia-api        
wiki_page_title = "Artificial Intelligence"  # Example Wikipedia page title
loader = WikipediaLoader(wiki_page_title,load_max_docs=2) # Load a maximum of 2 documents
wiki_documents = loader.load()
print(f"Number of Wikipedia documents loaded: {len(wiki_documents)}")
print(f"First Wikipedia document content: {wiki_documents[0].page_content[:500]}")  # Print first 500 characters of the first Wikipedia document

#Next step is to split the text into chunks for better processing and retrieval.