# Recommendation Systems

[![Notebooks](https://github.com/FelicienC/recommendation-systems/actions/workflows/notebooks.yml/badge.svg)](https://github.com/FelicienC/recommendation-systems/actions/workflows/notebooks.yml)
[![Docs](https://github.com/FelicienC/recommendation-systems/actions/workflows/docs.yml/badge.svg)](https://felicienc.github.io/recommendation-systems/)
[![License: MIT](https://img.shields.io/github/license/FelicienC/recommendation-systems)](https://github.com/FelicienC/recommendation-systems/blob/main/LICENSE)
![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

Recommendation systems are behind many of the things we use every day. This repo builds small Python simulations to understand how they work, one idea at a time. [📖 Read it online](https://felicienc.github.io/recommendation-systems/)

No black box and no magic: just data, intuition, and a bit of code 😄.


## The chapters

New to recommendation systems? Start with the [introduction](./src/recommendationsystems/introduction.md): what they are, how they work, and how recommendation differs from ranking.

Each chapter adds one new idea or tackles one new scaling challenge. We begin with the simplest setting, add richer sources of information, and finish with an architecture that serves recommendations in practice.

| | Chapter | What you learn |
|:-:|---|---|
| <img src="./src/recommendationsystems/01_bandits/images/platform_catalog.svg" width="260" alt="Contextual bandits"> | **01**<br>[Contextual bandits](https://felicienc.github.io/recommendation-systems/01_bandits/01_bandits.html) | Cold start: recommend with no history, balancing **exploration** and **exploitation**. |
| <img src="./src/recommendationsystems/02_content_based/images/cosine_similarity.svg" width="260" alt="Content-based"> | **02**<br>[Content-based](https://felicienc.github.io/recommendation-systems/02_content_based/02_content_based.html) | Recommend films that look like the ones you already like. |
| <img src="./src/recommendationsystems/03_collaborative_filtering/images/films_liked_together.svg" width="260" alt="Collaborative filtering"> | **03**<br>[Collaborative filtering](https://felicienc.github.io/recommendation-systems/03_collaborative_filtering/03_collaborative_filtering.html) | Learn from collective behavior: people like you, films liked together. |
| <img src="./src/recommendationsystems/04_two_towers/images/two_towers.svg" width="260" alt="Two towers"> | **04**<br>[Two towers](https://felicienc.github.io/recommendation-systems/04_two_towers/04_two_towers.html) | One vector per user, one per film: retrieval at scale, even for newcomers. |
| <img src="./src/recommendationsystems/05_sasrec/images/attention.svg" width="260" alt="SASRec"> | **05**<br>[SASRec](https://felicienc.github.io/recommendation-systems/05_sasrec/05_sasrec.html) | Order matters: self-attention reads your history to guess what comes next. |
| <img src="./src/recommendationsystems/06_lightgcn/images/likes_graph_network.svg" width="260" alt="LightGCN"> | **06**<br>[LightGCN](https://felicienc.github.io/recommendation-systems/06_lightgcn/06_lightgcn.html) | Users and films as a graph: vectors that walk along the likes. |
| <img src="./src/recommendationsystems/07_retrieval_ranking/images/funnel.svg" width="260" alt="Retrieval and ranking"> | **07**<br>[Retrieval and ranking](https://felicienc.github.io/recommendation-systems/07_retrieval_ranking/07_retrieval_ranking.html) | The production pipeline: cast a wide net, then sort the catch. |

## Run it locally

Install [uv](https://docs.astral.sh/uv/), run `make init`, then open any notebook with the `.venv` kernel (VS Code works out of the box).

## TODO: other techniques to cover

- **Bandits**: UCB and Thompson sampling.
- **Matrix factorization**: alternating least squares, and BPR for implicit feedback.
- **Factorization machines** and deep ranking models (Wide & Deep, DeepFM, DLRM).
- **Approximate nearest neighbor search** (HNSW, FAISS) to serve embeddings at scale.
- **Offline evaluation**: precision, recall, NDCG, and data leakage pitfalls.
- **Re-ranking**: diversity, novelty, and business rules.
- **Generative recommenders**: semantic IDs and LLM-based recommendations.
