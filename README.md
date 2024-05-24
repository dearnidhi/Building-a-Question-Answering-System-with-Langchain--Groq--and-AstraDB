Description:
This Python script demonstrates how to build a question-answering system using Langchain, Groq, and AstraDB. The system involves loading and processing web documents, generating embeddings, and setting up a vector store for efficient retrieval. Here’s a brief overview of the key steps:

Environment Setup: Load API keys and initialize the connection to AstraDB.
Web Document Loading: Use WebBaseLoader to fetch and parse content from a specified webpage.
Text Splitting: Apply RecursiveCharacterTextSplitter to divide large documents into manageable chunks.
Embeddings Generation: Utilize OpenAI embeddings to convert text documents into vector representations.
Vector Store Configuration: Configure a Cassandra vector store to manage and query document embeddings.
Model Initialization: Set up the Groq LLM model for generating answers.
Prompt Template: Define a chat prompt template to format the context and questions for the LLM.
Retrieval Chain: Create a retrieval chain that combines document retrieval and interaction with the LLM.
Example Query Function: Provide a template function to query the system and retrieve answers (commented out for demonstration purposes).
