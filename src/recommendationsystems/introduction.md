# Introduction

## What is a recommendation system?

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

## How does it work?

There is no single algorithm that works perfectly everywhere. Before choosing one, we need to understand the problem we are trying to solve:

- Do we know anything about the user, or do we only have an anonymous user ID?
- Do we know anything about the items, such as their category, author, or description?
- Do we have a history of clicks, views, ratings, or purchases?
- How many items are available?
- How quickly do we need to produce the recommendations?

For example, recommending a film to a new user is very different from recommending one to someone who has already watched hundreds of films. In the first case, we have very little information to work with. This is called **cold start**. The system has to make a good guess with almost no clues. Not the easiest place to start :)

This repository explores several ways to deal with these situations. We begin with simple simulations, then gradually move towards methods that are used in real production systems.

## What is the difference between recommendation and ranking?

These ideas are closely related, but they do not do exactly the same job.

A **ranking system** receives a known list of items and puts them in the most useful order. For example, a search engine may receive one thousand matching pages and rank them from the most relevant to the least relevant.

A **recommendation system** often has one extra job: deciding which items are worth considering in the first place. A large platform may have millions of items, so it first retrieves a smaller group of possible recommendations and then ranks them.

Think of it as a two-step process:

1. **Retrieval** finds a manageable set of possible items.
2. **Ranking** orders those items for the user.

The last chapter of this repository brings both steps together in a typical production pipeline.

Ready? Let's start with the first chapter: [contextual bandits](01_bandits/01_bandits.ipynb).
