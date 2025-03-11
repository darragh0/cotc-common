from enum import Enum


class PublisherRank(Enum):
    BEGINNER = 10
    INTERMEDIATE = 25
    ADVANCED = 50
    EXPERT = 75
    MASTER = 100
    LEGEND = 125
    GOD = 150

    @property
    def prev(self) -> "PublisherRank":
        if self == PublisherRank.BEGINNER:
            return self

        is_inter: bool = self == PublisherRank.INTERMEDIATE
        return PublisherRank(self.value - (15 if is_inter else 25))

    @property
    def next(self) -> "PublisherRank":
        if self == PublisherRank.GOD:
            return self
        
        is_beginner: bool = self == PublisherRank.BEGINNER
        return PublisherRank(self.value + (15 if is_beginner else 25))

