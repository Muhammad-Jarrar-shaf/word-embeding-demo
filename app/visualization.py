import matplotlib.pyplot as plt
import numpy as np
from sklearn.manifold import TSNE


def visualize_embeddings(service, words,
                           output_path="screenshots/embeddings_plot.png"):
    vectors = []
    labels = []

    for word in words:
        if service.word_exists(word):
            vectors.append(service.get_vector(word))
            labels.append(word)

    if len(vectors) < 2:
        raise ValueError("Need at least two valid words for visualization.")

    vectors = np.array(vectors)

    tsne = TSNE(
        n_components=2,
        random_state=42,
        perplexity=min(5, len(vectors) - 1)
    )

    reduced_vectors = tsne.fit_transform(vectors)

    plt.figure(figsize=(10, 8))

    for i, label in enumerate(labels):
        x, y = reduced_vectors[i]

        plt.scatter(x, y)
        plt.annotate(label, (x, y))

    plt.title("t-SNE Visualization of Word Embeddings")
    plt.xlabel("Dimension 1")
    plt.ylabel("Dimension 2")

    plt.tight_layout()

    plt.savefig(output_path)

    plt.close()

    return output_path