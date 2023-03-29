from datetime import date

from src.domain.common.services.sqlalchemy_service import AsyncSQLAlchemyService
from src.models import Statistic

from .dto import StatisticDto
from .entity import StatisticEntity
from .interfaces import StatisticRepositoryInterface
from .repository import StatisticRepository


class StatisticService(AsyncSQLAlchemyService[StatisticEntity, StatisticDto, None]):
    """
    Statistic Domain layer.
    """

    _repository: StatisticRepositoryInterface

    async def bulk_receive(
        self, from_: date | None = None, to: date | None = None, order_by: list[str] | None = None
    ) -> list[StatisticEntity]:
        return await self._repository.bulk_receive(from_=from_, to=to, order_by=order_by)

    async def delete_all(self) -> None:
        await self._repository.delete_all()


statistic_service = StatisticService(Statistic, StatisticEntity, repository=StatisticRepository)
