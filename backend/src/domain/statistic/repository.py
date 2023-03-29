from datetime import date

from sqlalchemy import select

from src.domain.common.repositories.sqlalchemy_repository import AsyncSQLAlchemyRepository
from src.models import Statistic

from .entity import StatisticEntity


class StatisticRepository(AsyncSQLAlchemyRepository):
    """
    Statistic Infrastructure layer.
    """

    async def bulk_receive(
        self, from_: date | None = None, to: date | None = None
    ) -> list[StatisticEntity]:
        async with self._session() as session:
            query = select(self._model)
            if from_:
                query = query.where(Statistic.date >= from_)
            if to:
                query = query.where(Statistic.date <= to)

            scalar_result = await session.scalars(query)

            rows = scalar_result.all()
            await session.commit()

        return rows
