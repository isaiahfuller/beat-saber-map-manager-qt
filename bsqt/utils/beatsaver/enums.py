from enum import Enum


class BeatSaverLatestSort(Enum):
    FIRST_PUBLISHED = 0
    UPDATED = 1
    LAST_PUBLISHED = 2
    CREATED = 3
    CURATED = 4
