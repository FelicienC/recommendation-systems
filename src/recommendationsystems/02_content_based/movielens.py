"""Load the MovieLens 100K dataset for the content-based recommendation example.

The dataset is provided by the GroupLens research group:
https://grouplens.org/datasets/movielens/100k/
"""

import urllib.request
import zipfile
from pathlib import Path

import numpy as np

DATASET_URL = "https://files.grouplens.org/datasets/movielens/ml-100k.zip"
DATASET_DIR = Path(".cache/ml-100k")

UserId = int
MovieId = int  # a film is identified by its row index


def _download() -> None:
    """Download and extract the dataset into `.cache`, once."""
    if DATASET_DIR.exists():
        return
    DATASET_DIR.parent.mkdir(exist_ok=True)
    archive_path = DATASET_DIR.parent / "ml-100k.zip"
    urllib.request.urlretrieve(DATASET_URL, archive_path)
    with zipfile.ZipFile(archive_path) as archive:
        archive.extractall(DATASET_DIR.parent)


def load_movies() -> tuple[list[str], list[str], np.ndarray]:
    """Return the genre names, the movie titles, and the movie-genre matrix.

    `titles[movie]` is the title and `genres[movie]` the 0/1 genre vector of
    the film with `MovieId` `movie`.
    """
    _download()
    genre_lines = (DATASET_DIR / "u.genre").read_text(encoding="latin-1").split()
    genre_names = [line.split("|")[0] for line in genre_lines]

    rows = (DATASET_DIR / "u.item").read_text(encoding="latin-1").splitlines()
    rows = [row.split("|") for row in rows]
    titles = [row[1] for row in rows]
    genres = np.array([row[5:] for row in rows], dtype=float)
    return genre_names, titles, genres


def load_ratings() -> np.ndarray:
    """Return one `(user, movie, rating)` row per rating, sorted by time."""
    _download()
    ratings = np.loadtxt(DATASET_DIR / "u.data", dtype=int)
    ratings = ratings[np.argsort(ratings[:, 3], kind="stable")]
    ratings[:, 1] -= 1  # movie ids start at 1, row indices at 0
    return ratings[:, :3]
