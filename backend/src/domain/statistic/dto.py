from datetime import date

from src.domain.common import BaseDTO


class StatisticDto(BaseDTO):
    date: date
    views: int | None
    clicks: int | None
    cost: float | None
