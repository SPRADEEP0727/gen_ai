### TEXT SPLITING AND CHUNKING ###
# This code demonstrates how to split text into chunks using LangChain's text splitter.
#chunk vs chunk overlap - chunk is a piece of text that is split from the original text, chunk overlap is the amount of text that is repeated in the next chunk.

#character text splitter for LangChain - means it splits text based on character count
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
PDF_file = "Articles.pdf"
loader = PyPDFLoader(PDF_file)
pdf_documents = loader.load()

full_text = "\n".join([doc.page_content for doc in pdf_documents])  # Combine all document contents into a single string
text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)  # Split text into chunks of 1000 characters with 200 characters overlap
chunks = text_splitter.split_text(full_text)


#recursive character text splitter for LangChain - means it splits text based on character count but also considers the structure of the text (like paragraphs, sentences, etc.)
# This is useful for maintaining the context of the text while splitting it into smaller chunks.
from langchain.text_splitter import RecursiveCharacterTextSplitter
recursive_text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,  # Size of each chunk in characters
    chunk_overlap=0,  # Overlap between chunks in characters
    length_function=len  # Function to determine the length of the text
)
recursive_chunks = recursive_text_splitter.split_documents(pdf_documents)  # Split the PDF documents into chunks
print(f"Number of chunks created: {len(recursive_chunks)}")
print(f"First chunk content: {recursive_chunks[0].page_content[:500]}")

#Next step is to use these chunks for further processing, such as embedding.