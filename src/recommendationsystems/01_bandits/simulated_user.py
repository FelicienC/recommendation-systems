"""The simulated user for the contextual bandit recommendation example.

We simulate simple predictable user behavior based on their characteristics,
to ensure the recommendation system is able to learn these preferences.
"""

import random
from dataclasses import dataclass
from enum import Enum

import numpy as np

random.seed(21)


class Nationality(Enum):
    """Define supported user nationalities."""

    US = "US"
    UK = "UK"
    FR = "FR"
    DE = "DE"
    JP = "JP"


class DeviceType(Enum):
    """Define supported device types."""

    MOBILE = "mobile"
    DESKTOP = "desktop"


class TimeOfDay(Enum):
    """Define supported time-of-day values."""

    MORNING = "morning"
    EVENING = "evening"
    OTHER = "other"


class ItemTitle(Enum):
    """Define supported item titles."""

    TECHNOLOGY = "Technology"
    SPORTS = "Sports"
    CUISINE = "Cuisine"
    CAR = "Car"
    ART = "Art"


@dataclass(frozen=True)
class User:
    """Represent a simulated user."""

    nationality: Nationality
    time_of_day: TimeOfDay
    device_type: DeviceType
    age: int


@dataclass
class Item:
    """Represent one item in the catalog."""

    title: ItemTitle


def random_user() -> User:
    """Create one user from the simulator's supported values."""
    return User(
        nationality=random.choice(tuple(Nationality)),
        time_of_day=random.choice(tuple(TimeOfDay)),
        device_type=random.choice(tuple(DeviceType)),
        age=random.randint(18, 70),
    )


def user_to_features(user: User) -> np.ndarray:
    """Convert a simulated user into a numeric feature vector."""
    features = [1.0]
    features += [float(user.nationality == value) for value in Nationality]
    features += [float(user.time_of_day == value) for value in TimeOfDay]
    features += [float(user.device_type == value) for value in DeviceType]
    features += [(user.age - 44.0) / 26.0]
    return np.array(features)


def rate_item_deterministic(user: User, item: Item) -> int:
    """Rate an item using the simulator's deterministic preferences.

    French users prefer Cuisine streams in the morning and Technology streams
    in the evening.
    American users prefer Technology streams in the morning and Sports streams
    in the evening.
    German users prefer Car streams on mobile, and Sports streams on desktop.
    Japanese users prefer Art streams in the morning and Technology streams in
    the evening.
    British users prefer Sports streams on mobile, and Cuisine streams on desktop.

    Ratings are on a scale from 1 to 5.
    """
    preference_rules = {
        Nationality.FR: (
            (ItemTitle.CUISINE, user.time_of_day == TimeOfDay.MORNING),
            (ItemTitle.TECHNOLOGY, user.time_of_day == TimeOfDay.EVENING),
        ),
        Nationality.US: (
            (ItemTitle.TECHNOLOGY, user.time_of_day == TimeOfDay.MORNING),
            (ItemTitle.SPORTS, user.time_of_day == TimeOfDay.EVENING),
        ),
        Nationality.DE: (
            (ItemTitle.CAR, user.device_type == DeviceType.MOBILE),
            (ItemTitle.SPORTS, user.device_type == DeviceType.DESKTOP),
        ),
        Nationality.JP: (
            (ItemTitle.ART, user.time_of_day == TimeOfDay.MORNING),
            (ItemTitle.TECHNOLOGY, user.time_of_day == TimeOfDay.EVENING),
        ),
        Nationality.UK: (
            (ItemTitle.SPORTS, user.device_type == DeviceType.MOBILE),
            (ItemTitle.CUISINE, user.device_type == DeviceType.DESKTOP),
        ),
    }
    return (
        5
        if any(
            item.title == preferred_item and matches
            for preferred_item, matches in preference_rules[user.nationality]
        )
        else 3
    )


def rate_item(user: User, item: Item) -> int:
    """Rate an item with some randomness added to simulate imperfect human behavior."""
    base_rating = rate_item_deterministic(user, item)
    age_centered = (user.age - 44.0) / 26.0
    age_sensitivity = {
        ItemTitle.TECHNOLOGY: -1.0,
        ItemTitle.SPORTS: -0.5,
        ItemTitle.CUISINE: 0.25,
        ItemTitle.CAR: 0.5,
        ItemTitle.ART: 0.75,
    }[item.title]
    noise = random.choice([-1, 0, 1])
    return max(1, min(5, round(base_rating + age_centered * age_sensitivity + noise)))
