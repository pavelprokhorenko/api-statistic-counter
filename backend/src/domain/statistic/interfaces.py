from abc import ABCMeta
from datetime import date

from src.domain.common.interfaces import AsyncDBRepositoryInterface
from src.domain.common.typevars import Model


class StatisticRepositoryInterface(AsyncDBRepositoryInterface, metaclass=ABCMeta):
    async def bulk_receive(
        self, from_: date | None = None, to: date | None = None, order_by: list[str] | None = None
    ) -> list[Model]:
        """
        Receive multiple rows with filters by date.
        """

    async def delete_all(self) -> None:
        """
        Delete all data.
        """
