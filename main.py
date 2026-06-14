from app.api import app
from app.embedding_service import EmbeddingService
from app.visualization import visualize_embeddings

service = EmbeddingService()

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

output_file = visualize_embeddings(service, words)

print(f"Visualization saved to: {output_file}")