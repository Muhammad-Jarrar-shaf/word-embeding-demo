from app.embedding_service import EmbeddingService

service = EmbeddingService()


def test_word_exists():
    assert service.word_exists("king") is True


def test_nonexistent_word():
    assert service.word_exists("qwertyasdfgh") is False


def test_similar_words():
    results = service.get_similar_words("king")

    assert results is not None
    assert len(results) > 0