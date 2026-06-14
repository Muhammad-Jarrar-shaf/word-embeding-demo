import gensim.downloader as api


class EmbeddingService:
    def __init__(self):
        print("Loading embeddings...")
        self.model = api.load("glove-wiki-gigaword-50")
        print("Embeddings loaded successfully!")

    def get_similar_words(self, word, top_n=5):
        try:
            return self.model.most_similar(word, topn=top_n)
        except KeyError:
            return None

    def word_exists(self, word):
        return word in self.model.key_to_index

    def get_vector(self, word):
        if self.word_exists(word):
            return self.model[word]
        return None