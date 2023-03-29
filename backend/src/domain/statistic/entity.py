from collections.abc import Mapping
from datetime import date
from typing import Any

from pydantic import validator

from src.domain.common import Entity


class StatisticEntity(Entity):
    id: int
    date: date
    views: int | None
    clicks: int | None
    cost: float | None

    cpc: float | None
    cpm: float | None

    @validator("cpc", always=True, pre=True)
    def count_cpc(cls, v: float | None, values: Mapping[str, Any]) -> float:
        cost = values.get("cost")
        clicks = values.get("clicks")

        if cost and clicks:
            return cost / clicks
        return v

    @validator("cpm", always=True, pre=True)
    def count_cpm(cls, v: float | None, values: Mapping[str, Any]) -> float:
        cost = values.get("cost")
        views = values.get("views")

        if cost and views:
            return cost / views * 1000
        return v
