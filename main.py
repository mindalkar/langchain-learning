from dotenv import load_dotenv
import os
from langchain_unstructured import UnstructuredLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

load_dotenv()

def main():
    print("Hello from langchain-learning!")
    loader = UnstructuredLoader(
            file_path = "/Users/mayurindalkar/Documents/learning/langchain/langchain-learning/mediumblog1.txt",
            chunking_strategy="basic",
            max_characters=1000000
        )
    document = loader.load()

    print("splitting ....")

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)

    texts = text_splitter.split_documents(documents=document)

    print(f"Create {len(texts)} documents")

    embeddings = OpenAIEmbeddings(openai_api_key=os.environ["OPENAI_API_KEY"])

    print("ingesting....")

    PineconeVectorStore.from_documents(texts, embeddings, index_name=os.environ["INDEX_NAME"])

if __name__ == "__main__":
    main()
