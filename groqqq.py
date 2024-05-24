import os
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter  # Import RecursiveCharacterTextSplitter class
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.vectorstores.cassandra import Cassandra
import cassio
import bs4
from dotenv import load_dotenv
load_dotenv()

# Load Groq API key from environment variable
groq_api_key = os.environ['GROQ_API_KEY']

# Connection to the ASTRA DB
ASTRA_DB_APPLICATION_TOKEN = "AstraCS:mxOZPsEwppSOIXpaFyxJLOFw:8806b6b022eb91ca65c09c2551dc1aef9b7688783fc1b5f78405d6c916b4c154"  # Replace with your actual token
ASTRA_DB_ID = "0b1b2d72-aefd-4b4a-abb0-bb0aa6132042"  # Replace with your actual database ID

# Initialize connection to AstraDB
cassio.init(token=ASTRA_DB_APPLICATION_TOKEN, database_id=ASTRA_DB_ID)

# Define web document loader with specific parsing options
loader = WebBaseLoader(
    web_paths=["https://lilianweng.github.io/posts/2023-06-23-agent/"],
    bs_kwargs=dict(parse_only=bs4.SoupStrainer(class_=("post-title", "post-content", "post-header")))
)

# Load text documents from the web page
text_documents = loader.load()

# Text splitter for dividing large documents into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs = text_splitter.split_documents(text_documents)

# Install required libraries (assuming not already installed)
# !pip install cassandra-driver openai

# OpenAI embeddings for generating document vectors
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
embeddings = OpenAIEmbeddings()

# AstraDB vector store configuration
astra_vector_store = Cassandra(
    embedding=embeddings,
    table_name="qa_mini_demo",
    session=None,
    keyspace=None
)

# Create vector store index wrapper
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
astra_vector_index = VectorStoreIndexWrapper(vectorstore=astra_vector_store)

# Initialize Groq LLM model
llm = ChatGroq(groq_api_key=groq_api_key, model_name="mixtral-8x7b-32768")

# Chat prompt template defining the format for context and questions
from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_template("""
Answer the following question based only on the provided context.
Think step by step before providing a detailed answer.
I will tip you $1000 if the user finds the answer helpful.

<context>
{context}
</context>

Question: {input}""")

# Example query using the vector store index (uncomment to test)
# astra_vector_index.query("Chain of thought (CoT; Wei et al. 2022) has become a standard prompting technique", llm=llm)

# Retrieval chain for combining document retrieval and interaction with Groq
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

retriever = astra_vector_store.as_retriever()
document_chain = create_stuff_documents_chain(llm, prompt)
retrieval_chain = create_retrieval_chain(retriever, document_chain)

# Example function to answer a question using the retrieval chain (uncomment to test)
# def answer_question(question):
#     response = retrieval_chain.invoke({"input": question})
#     return response

# Integrate with a web framework (e.g., Streamlit) for user interaction (not included)