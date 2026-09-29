# Recommendation Systems Explained

Recommendation systems are behind many of the things we use every day. In this repository, we build small Python simulations to understand how they work, one idea at a time. No black box and no magic: just data, intuition, and a bit of code :)

Read it online: https://felicienc.github.io/recommendation-systems/

Or run the notebooks locally: install [uv](https://docs.astral.sh/uv/), run `make init`, then open any notebook with the `.venv` kernel (VS Code works out of the box).

## Introduction

### What is a recommendation system?

You open Netflix and see a list of films you might enjoy. You start Spotify and find a playlist that seems to know you. You visit Amazon and discover a product you were apparently about to buy.

Behind these suggestions is a recommendation system.

Its job can be summed up with one simple question:

> Given a user and a collection of items, which items should we show this user?

An item can be almost anything: a film, a song, a product, an article, a video, or even another user to follow. The system looks at what it knows about the user, the items, and their past interactions, then uses that information to make better suggestions.

Here are a few examples we meet every day:

- Netflix recommends films and series.
- Spotify recommends songs, albums, and playlists.
- Amazon recommends products.
- YouTube recommends videos.
- A news application recommends articles.

The objective can change from one platform to another. Maybe we want to help users discover something relevant, increase purchases, keep them coming back, or simply make the service easier to use.

### How does it work?

There is no single algorithm that works perfectly everywhere. Before choosing one, we need to understand the problem we are trying to solve:

- Do we know anything about the user, or do we only have an anonymous user ID?
- Do we know anything about the items, such as their category, author, or description?
- Do we have a history of clicks, views, ratings, or purchases?
- How many items are available?
- How quickly do we need to produce the recommendations?

For example, recommending a film to a new user is very different from recommending one to someone who has already watched hundreds of films. In the first case, we have very little information to work with. This is called **cold start**. The system has to make a good guess with almost no clues. Not the easiest place to start :)

This repository explores several ways to deal with these situations. We begin with simple simulations, then gradually move towards methods that are used in real production systems.

### What is the difference between recommendation and ranking?

These ideas are closely related, but they do not do exactly the same job.

A **ranking system** receives a known list of items and puts them in the most useful order. For example, a search engine may receive one thousand matching pages and rank them from the most relevant to the least relevant.

A **recommendation system** often has one extra job: deciding which items are worth considering in the first place. A large platform may have millions of items, so it first retrieves a smaller group of possible recommendations and then ranks them.

Think of it as a two-step process:

1. **Retrieval** finds a manageable set of possible items.
2. **Ranking** orders those items for the user.

The last chapter of this repository brings both steps together in a typical production pipeline.

## A progressive tour of recommendation systems

Now for the tour. As we move through the repository, we give the system more information and better ways to represent users, items, and their interactions. Each chapter adds one new idea or tackles one new scaling challenge.

1. **[Contextual bandits](./src/recommendationsystems/01_bandits)**: We start with the cold-start problem. A bandit has to decide what to show while balancing **exploration** of new options with **exploitation** of what already works.
2. **[Content-based recommendations](./src/recommendationsystems/02_content_based)**: Next, we use information about the items and the user. A film can be recommended because it shares characteristics with films the user already likes, even when interaction history is limited.
3. **[Collaborative filtering](./src/recommendationsystems/03_collaborative_filtering)**: Once we have enough historical interactions, we can learn from collective behavior. Users with similar tastes, and films liked by the same people, point to good recommendations without needing any item description.
4. **[Two-tower models](./src/recommendationsystems/04_two_towers)**: As the number of users and items grows, we need representations that can be compared efficiently. Two-tower models learn user and item embeddings separately, which makes large-scale candidate retrieval possible.
5. **[SASRec](./src/recommendationsystems/05_sasrec)**: User behavior also has an order. Self-attentive sequential recommendation uses a user's recent history to understand what they may want next.
6. **[LightGCN](./src/recommendationsystems/06_lightgcn)**: Users and items can be viewed as a graph connected by interactions. Graph neural networks use those connections to capture relationships that may be missed when we look at each interaction separately.
7. **[Retrieval and ranking](./src/recommendationsystems/07_retrieval_ranking)**: Finally, we bring everything together in a production pipeline. Retrieval finds a small set of promising candidates, and ranking orders them for the user.

The order is intentional. We begin with the simplest setting, add richer sources of information, and finish with an architecture that can serve recommendations efficiently in practice.

## TODO: other techniques to cover

- **Bandits**: UCB and Thompson sampling.
- **Matrix factorization**: alternating least squares, and BPR for implicit feedback.
- **Factorization machines** and deep ranking models (Wide & Deep, DeepFM, DLRM).
- **Approximate nearest neighbor search** (HNSW, FAISS) to serve embeddings at scale.
- **Offline evaluation**: precision, recall, NDCG, and data leakage pitfalls.
- **Re-ranking**: diversity, novelty, and business rules.
- **Generative recommenders**: semantic IDs and LLM-based recommendations.
