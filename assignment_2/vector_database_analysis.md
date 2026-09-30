
````markdown
# Vector Databases

## What is a Vector Database?

An embedding model changes text or images into a list of numbers called a vector.

Things with similar meaning get similar vectors.

A vector database stores these vectors and can quickly find the vectors closest to a question.

This means that it searches by meaning, not just by matching exact words.

For example, a user may ask:

"How do I recover my account?"

A vector search can find a document such as:

"Reset your password"

even though the exact words are different.

## How Vector Search Works

```text
Documents
    |
    v
Text Chunking
    |
    v
Embedding Model
    |
    v
Vector Database
    |
    v
Similarity Search
    |
    v
Relevant Chunks
    |
    v
LLM
    |
    v
Final Answer
````

First, documents are divided into smaller chunks.

The embedding model converts each chunk into a numerical vector.

These vectors are stored in the vector database.

When a user asks a question, the question is also converted into a vector.

The vector database then finds the most similar vectors and returns the relevant document chunks.

## Similarity Search

Checking every stored vector individually can become slow when the database contains a large number of vectors.

Vector databases can use approximate nearest-neighbor indexes such as HNSW to find very close matches efficiently.

They can also filter results using additional information such as language or category.

For example:

```json
{
    "crop": "tomato",
    "language": "Hindi"
}
```

This allows the system to search for relevant information while also filtering by crop or language.

# Popular Vector Databases

| Database | Good For                         | Weak Point                              |
| -------- | -------------------------------- | --------------------------------------- |
| FAISS    | Very fast experiments            | No built-in storage server or filtering |
| Chroma   | Easy to start, small projects    | Better suited for smaller applications  |
| Pinecone | Fully managed systems            | Costs money                             |
| Milvus   | Very large collections           | More complex to set up                  |
| Qdrant   | Fast search and strong filtering | Smaller community                       |
| pgvector | PostgreSQL applications          | Better when PostgreSQL is already used  |

# My Example Problem

I would build a chatbot that helps farmers with crop diseases in English and Hindi.

The chatbot would support:

* Tomato
* Potato
* Corn

The system would contain approximately 50,000 text chunks.

It should:

* Search information based on semantic meaning.
* Filter results by crop.
* Filter results by language.
* Run with a relatively low budget.
* Be easy to update.
* Support additional crops and regions in the future.

# My Choice: Qdrant

For this hypothetical problem, I would choose **Qdrant** and run it on our own server using Docker.

## Why Qdrant?

### 1. Vector Search

Qdrant is designed for storing and searching vector embeddings efficiently.

This makes it suitable for the semantic search required by the farmer chatbot.

### 2. Metadata Filtering

The system can store additional information with each vector.

For example:

```json
{
    "crop": "tomato",
    "language": "Hindi"
}
```

The chatbot can therefore search for relevant information while filtering results by crop and language.

### 3. Open Source

Qdrant is free and open source and can be self-hosted.

This makes it suitable for a low-budget project.

### 4. Easy Deployment

Qdrant can be deployed using Docker, making it convenient to set up and manage.

### 5. Easy Updates

Documents can be added, changed or deleted without rebuilding the entire system.

### 6. Scalability

The system can grow if more crops, regions or documents are added later.

# Proposed Architecture

```text
Farmer Question
       |
       v
Multilingual Embedding Model
       |
       v
Qdrant Vector Database
       |
       +---- Filter: Crop
       |
       +---- Filter: Language
       |
       v
Top Relevant Results
       |
       v
Re-ranking
       |
       v
Top 5 Results
       |
       v
LLM
       |
       v
Answer in English/Hindi
```

## Embedding Model

Since the chatbot needs to support both English and Hindi, I would use a multilingual embedding model.

The embedding model would convert the farmer's question and stored document chunks into vectors that can be compared using semantic similarity.

## Search Configuration

For this system, I would use:

* HNSW index
* Cosine similarity
* Crop metadata filtering
* Language metadata filtering
* Re-ranking of retrieved results

The system could retrieve the top 20 relevant results and then re-rank them before sending the best 5 results to the LLM.

# Why Not the Other Options?

### FAISS

FAISS is useful for fast local experiments, but it does not have the same built-in filtering capabilities required for this application.

### Chroma

Chroma is easy to start with and is suitable for smaller projects.

### Pinecone

Pinecone provides a managed service, but hosting costs may be less suitable for a low-budget project.

### Milvus

Milvus is suitable for very large vector collections, but it would add more deployment complexity for this particular use case.

### pgvector

pgvector would be a good choice if the application already used PostgreSQL extensively.

For this standalone vector-search system, I would use Qdrant.

# Conclusion

For the hypothetical multilingual crop-disease chatbot, I would choose Qdrant because it provides vector similarity search, metadata filtering, self-hosting, easy deployment and convenient document updates.

The overall system would use a multilingual embedding model, Qdrant for vector search, metadata filters for crop and language, re-ranking for better retrieval, and an LLM to generate the final answer.

```

### 3. Scroll down

Click:

**Commit changes**

Then **Step 9 is finished.** Your uploaded assignment also uses the farmer crop-disease chatbot and Qdrant selection as the example problem and choice. :contentReference[oaicite:0]{index=0}
```
