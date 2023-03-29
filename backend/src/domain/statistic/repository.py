from datetime import date

from sqlalchemy import delete, select

from src.domain.common.repositories.sqlalchemy_repository import AsyncSQLAlchemyRepository

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
                query = query.where(self._model.date >= from_)
            if to:
                query = query.where(self._model.date <= to)

            scalar_result = await session.scalars(query)

            rows = scalar_result.all()
            await session.commit()

        return rows

    async def delete_all(self) -> None:
        async with self._session() as session:
            query = delete(self._model)
            await session.execute(query)
            await session.commit()
