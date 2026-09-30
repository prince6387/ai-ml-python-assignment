
# LLM Chatbot Architecture

## Introduction

A chatbot based on a Large Language Model (LLM) is more than just a language model. A complete system requires a user interface, backend orchestration, memory, retrieval, embeddings, a vector database, the LLM itself, guardrails, and monitoring.

For applications that need to answer questions from private or frequently changing documents, I would use Retrieval-Augmented Generation (RAG).

## High-Level Architecture

```text
User
  |
  v
User Interface
  |
  v
Backend / Orchestrator
  |
  +------> Input Guardrails
  |
  +------> Chat Memory
  |
  +------> Retriever
              |
              v
        Vector Database
              |
              v
       Relevant Documents
              |
              v
        Prompt Builder
              |
              v
             LLM
              |
              v
       Output Guardrails
              |
              v
       Final Response
````

## Main Components

### 1. User Interface

The user interface is the website or application where the user enters a question.

Examples include:

* Web application
* Mobile application
* Streamlit application

The interface sends the user's question to the backend.

### 2. Backend / Orchestrator

The backend controls the complete workflow.

It can handle:

* API requests
* Authentication
* Conversation management
* Retrieval
* Prompt construction
* LLM requests
* Tool calls

Python frameworks such as FastAPI or Flask can be used to implement the backend.

### 3. Input Guardrails

Input guardrails validate the user's question before processing it.

They can help identify:

* Harmful requests
* Off-topic questions
* Sensitive information
* Invalid inputs
* Prompt injection attempts

### 4. Document Ingestion Pipeline

For a RAG chatbot, documents need to be prepared before they can be searched.

The pipeline can be:

```text
Documents
    |
    v
Text Extraction
    |
    v
Text Chunking
    |
    v
Embedding Model
    |
    v
Vector Database
```

Documents can include PDFs, web pages, Word documents or database records.

The documents are divided into smaller chunks so that relevant information can be retrieved efficiently.

### 5. Embedding Model

An embedding model converts text into numerical vectors.

For example:

```text
"How do I apply for leave?"
             |
             v
       Embedding Model
             |
             v
    [0.21, -0.14, 0.72, ...]
```

Texts with similar meanings generally have similar vector representations.

### 6. Vector Database

The generated embeddings are stored in a vector database.

When a user asks a question, the question is also converted into an embedding.

The vector database then searches for similar vectors and returns relevant document chunks.

Examples of vector databases include:

* Qdrant
* Pinecone
* Chroma
* Milvus
* pgvector

### 7. Retriever and Re-ranker

The retriever searches the vector database and returns potentially relevant documents.

A re-ranker can then rank the retrieved documents based on their relevance to the user's question.

This helps provide the LLM with better context.

### 8. Prompt Builder

The prompt builder combines the different pieces of information required by the LLM.

For example:

```text
System Instructions
        +
Conversation History
        +
Retrieved Documents
        +
User Question
        |
        v
      Prompt
```

The final prompt is sent to the LLM.

### 9. Chat Memory

Chat memory stores relevant previous messages.

For example:

```text
User: What is machine learning?

Bot: Machine learning is a branch of AI...

User: Give me an example.

Bot: One example is spam email detection.
```

The second question depends on the previous conversation.

### 10. LLM

The Large Language Model receives the prompt and generates the final response.

The LLM can be accessed through an API or deployed using a suitable model infrastructure depending on the application's requirements.

### 11. Tools and APIs

The chatbot can also use external tools.

For example:

* Database queries
* Weather APIs
* Search APIs
* Calculator
* Internal company APIs

This allows the chatbot to perform actions instead of only generating text.

### 12. Output Guardrails

The generated answer can be checked before being displayed to the user.

Output guardrails can help with:

* Safety
* Privacy
* Hallucination detection
* Formatting
* Source attribution

### 13. Monitoring and Evaluation

A production chatbot should be monitored continuously.

Important metrics include:

* Response latency
* API cost
* Retrieval quality
* Answer quality
* Error rate
* User feedback

Evaluation can be used to improve the chatbot over time.

## How One Question Is Answered

The complete process can be summarized as follows:

1. The user asks a question.
2. The question passes through input guardrails.
3. The question is converted into an embedding.
4. The vector database searches for similar document chunks.
5. The most relevant chunks are retrieved.
6. The question, retrieved information and conversation history are added to the prompt.
7. The prompt is sent to the LLM.
8. The LLM generates an answer.
9. Output guardrails check the answer.
10. The final answer is shown to the user, optionally with sources.

## Why Use RAG?

RAG is useful for applications that need domain-specific or frequently changing information.

The main advantages are:

* New information can be added without retraining the LLM.
* The LLM receives relevant external context.
* Private company or organization documents can be used.
* Responses can include sources from the retrieved documents.
* The knowledge base can be updated independently of the LLM.

## Summary

A production-ready LLM chatbot consists of multiple components working together. The LLM is the core language-generation component, while the backend, memory, retrieval system, vector database, guardrails and monitoring make the overall application useful and reliable.

For a knowledge-based chatbot, I would use a RAG architecture where documents are converted into embeddings, stored in a vector database, retrieved based on the user's question, and provided as context to the LLM.
