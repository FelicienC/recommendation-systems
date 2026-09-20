"""The simulated user for the contextual bandit recommendation example.

We simulate simple predictable user behavior based on their characteristics,
to ensure the recommendation system is able to learn these preferences.
"""

import random
from dataclasses import dataclass
from enum import Enum

import numpy as np

random.seed(21)  # Keep notebook output reproducible


class Country(Enum):
    """Define supported user countries."""

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


class Item(Enum):
    """Define supported recommendation items."""

    TECHNOLOGY = "Technology"
    SPORTS = "Sports"
    CUISINE = "Cuisine"
    CAR = "Car"
    ART = "Art"


@dataclass(frozen=True)
class User:
    """Represent a simulated user."""

    country: Country
    time_of_day: TimeOfDay
    device_type: DeviceType
    age: int

    def __repr__(self) -> str:
        """Return a string representation of the user."""
        return (
            f"User(country={self.country.value}, "
            f"time_of_day={self.time_of_day.value}, "
            f"device_type={self.device_type.value}, "
            f"age={self.age})"
        )


def random_user() -> User:
    """Create one user from the simulator's supported values."""
    return User(
        country=random.choice(tuple(Country)),
        time_of_day=random.choice(tuple(TimeOfDay)),
        device_type=random.choice(tuple(DeviceType)),
        age=random.randint(18, 70),
    )


def user_to_features(user: User) -> np.ndarray:
    """Convert a simulated user into a numeric feature vector."""
    features = [1.0]
    features += [float(user.country == value) for value in Country]
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
        Country.FR: (
            (Item.CUISINE, user.time_of_day == TimeOfDay.MORNING),
            (Item.TECHNOLOGY, user.time_of_day == TimeOfDay.EVENING),
        ),
        Country.US: (
            (Item.TECHNOLOGY, user.time_of_day == TimeOfDay.MORNING),
            (Item.SPORTS, user.time_of_day == TimeOfDay.EVENING),
        ),
        Country.DE: (
            (Item.CAR, user.device_type == DeviceType.MOBILE),
            (Item.SPORTS, user.device_type == DeviceType.DESKTOP),
        ),
        Country.JP: (
            (Item.ART, user.time_of_day == TimeOfDay.MORNING),
            (Item.TECHNOLOGY, user.time_of_day == TimeOfDay.EVENING),
        ),
        Country.UK: (
            (Item.SPORTS, user.device_type == DeviceType.MOBILE),
            (Item.CUISINE, user.device_type == DeviceType.DESKTOP),
        ),
    }
    return (
        5
        if any(
            item == preferred_item and matches
            for preferred_item, matches in preference_rules[user.country]
        )
        else 3
    )


def rate_item(user: User, item: Item) -> int:
    """Rate an item with some randomness added to simulate imperfect human behavior."""
    base_rating = rate_item_deterministic(user, item)
    age_centered = (user.age - 44.0) / 26.0
    age_sensitivity = {
        Item.TECHNOLOGY: -1.0,
        Item.SPORTS: -0.5,
        Item.CUISINE: 0.25,
        Item.CAR: 0.5,
        Item.ART: 0.75,
    }[item]
    noise = random.choice([-1, 0, 1])
    return max(1, min(5, round(base_rating + age_centered * age_sensitivity + noise)))
