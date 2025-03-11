from enum import Enum


class PublisherRank(Enum):
    BEGINNER = 10
    INTERMEDIATE = 25
    ADVANCED = 50
    EXPERT = 75
    MASTER = 100
    LEGEND = 125
    GOD = 150

    def prev(self) -> "PublisherRank":
        if self == PublisherRank.BEGINNER:
            return self
        return PublisherRank(self.value - 1)

    def next(self) -> "PublisherRank":
        if self == PublisherRank.GOD:
            return self
        return PublisherRank(self.value + 1)
