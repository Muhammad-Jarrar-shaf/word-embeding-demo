from fastapi import FastAPI, HTTPException
from app.embedding_service import EmbeddingService
from app.visualization import visualize_embeddings

app = FastAPI(
    title="Word Embedding Demo",
    description="Explore semantic relationships using pre-trained word embeddings.",
    version="1.0.0"
)

service = EmbeddingService()


@app.get("/")
def root():
    return {
        "message": "Word Embedding Demo API is running."
    }


@app.get("/similar")
def similar_words(word: str, top_n: int = 5):
    results = service.get_similar_words(word, top_n)

    if results is None:
        raise HTTPException(
            status_code=404,
            detail=f"'{word}' not found in vocabulary."
        )

    return {
        "word": word,
        "similar_words": [
            {
                "word": similar_word,
                "score": round(score, 4)
            }
            for similar_word, score in results
        ]
    }


@app.get("/visualize")
def generate_visualization():
    words = [
        "king",
        "queen",
        "prince",
        "princess",
        "man",
        "woman",
        "dog",
        "cat",
        "lion",
        "tiger",
        "python",
        "java",
        "linux",
        "computer",
        "internet"
    ]

    output_path = visualize_embeddings(service, words)

    return {
        "message": "Visualization generated successfully.",
        "path": output_path
    }