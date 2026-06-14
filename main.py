from app.embedding_service import EmbeddingService

service = EmbeddingService()

word = "king"

results = service.get_similar_words(word)

print(f"\nWords similar to '{word}':")

for similar_word, score in results:
    print(f"{similar_word}: {score:.4f}")