from src.domain.common.services.sqlalchemy_service import AsyncSQLAlchemyService
from src.models import Statistic

from .dto import StatisticDto
from .entity import StatisticEntity


class StatisticService(AsyncSQLAlchemyService[StatisticEntity, StatisticDto]):
    """
    Statistic Domain.
    """


statistic_service = StatisticService(model=Statistic, entity=StatisticEntity)
