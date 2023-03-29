from datetime import date

from src.domain.common.services.sqlalchemy_service import AsyncSQLAlchemyService
from src.models import Statistic

from .dto import StatisticDto
from .entity import StatisticEntity
from .repository import StatisticRepository


class StatisticService(AsyncSQLAlchemyService[StatisticEntity, StatisticDto, None]):
    """
    Statistic Domain layer.
    """

    _repository: StatisticRepository

    async def bulk_receive(
        self, from_: date | None = None, to: date | None = None
    ) -> list[StatisticEntity]:
        return await self._repository.bulk_receive(from_=from_, to=to)

    async def delete_all(self) -> None:
        await self._repository.delete_all()


statistic_service = StatisticService(Statistic, StatisticEntity, repository=StatisticRepository)
