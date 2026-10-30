
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def run_semantic_search():
    # Define a collection of text documents
    documents = [
        "Students can register courses through the student portal.",
        "The examination office publishes examination schedules.",
        "The finance office handles tuition fee issues.",
        "The library provides digital research resources.",
    ]

    query = "Where can I register my courses?"

    # Load the sentence transformer model
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    # Generate document and query embeddings
    document_embeddings = model.encode(documents)
    query_embedding = model.encode([query])

    # Calculate similarity scores between query and all documents
    scores = cosine_similarity(query_embedding, document_embeddings)[0]

    # Rank documents by similarity score in descending order
    results = sorted(
        zip(documents, scores),
        key=lambda item: item[1],
        reverse=True,
    )

    print(f"Query: '{query}'\n")
    print("Ranked Search Results:")
    for document, score in results:
        print(f"{score:.4f} -> {document}")

if __name__ == "__main__":
    run_semantic_search()