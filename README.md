# Word Embedding Demo

A FastAPI-powered NLP application that demonstrates semantic relationships between words using pre-trained GloVe embeddings and t-SNE visualization.

## Project Overview

This project explores one of the foundational concepts in Natural Language Processing (NLP): **word embeddings**. Traditional NLP approaches represented words independently, whereas word embeddings map words into dense vector spaces where semantic relationships emerge naturally.

The application allows users to:

* Find semantically similar words using pre-trained embeddings.
* Visualize high-dimensional word vectors using t-SNE.
* Access functionality through a FastAPI-based REST API.
* Explore automatically generated API documentation via Swagger UI.

---

## Features

* Semantic similarity search using GloVe embeddings
* Word vector retrieval
* t-SNE dimensionality reduction and visualization
* FastAPI integration with interactive Swagger documentation
* Automated testing with Pytest
* Modular and professional project structure

---

## Tech Stack

* Python
* FastAPI
* Gensim
* Scikit-learn
* Matplotlib
* Pytest
* Uvicorn

---

## Project Structure

```text
word-embedding-demo/
│
├── app/
│   ├── api.py
│   ├── embedding_service.py
│   ├── visualization.py
│   └── utils.py
│
├── tests/
│   ├── test_api.py
│   └── test_embeddings.py
│
├── screenshots/
├── notebooks/
├── requirements.txt
├── README.md
└── main.py
```

---

## Installation

```bash
git clone https://github.com/Muhammad-Jarrar-shaf/word-embeding-demo.git

cd word-embeding-demo

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

---

## Running the API

```bash
uvicorn app.api:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Root Endpoint

```
GET /
```

Health check endpoint.

---

### Similar Words

```
GET /similar?word=king
```

Example Response:

```json
{
    "word": "king",
    "similar_words": [
        {
            "word": "queen",
            "score": 0.85
        }
    ]
}
```

---

### Generate Visualization

```
GET /visualize
```

Generates a t-SNE visualization of selected word embeddings.

---

## Testing

Run automated tests using:

```bash
pytest -v
```

---

## Key Learnings

* Understanding distributed word representations
* Working with pre-trained embeddings
* Implementing dimensionality reduction using t-SNE
* Building ML-powered APIs with FastAPI
* Writing automated tests for NLP applications
* Debugging Python packaging and ML integration issues

---

## Screenshots

Include screenshots of:

* Swagger UI
* t-SNE visualization output
* Similarity endpoint responses

---

## Future Improvements

* Support custom user-provided word lists
* Add Word2Vec training on custom corpora
* Deploy using Docker
* Build an interactive frontend for visualization

---

## License

This project is part of the **100 Projects in 100 Days Challenge** focused on strengthening AI/ML engineering skills through hands-on development.
