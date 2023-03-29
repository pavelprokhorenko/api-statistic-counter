from datetime import date

from fastapi import APIRouter, Body, Query, status

from src.domain.statistic import StatisticDto, StatisticEntity, statistic_service

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[StatisticEntity])
async def receive_statistics(
    from_: date | None = Query(None, alias="from"),
    to: date | None = Query(None),
    order_by: list[str] | None = Query(None),
) -> list[StatisticEntity]:
    """
    Retrieve statistics.
    """
    return await statistic_service.bulk_receive(from_=from_, to=to, order_by=order_by)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=list[StatisticEntity])
async def bulk_create_statistic(
    statistics: list[StatisticDto] = Body(...),
) -> list[StatisticEntity]:
    """
    Create new statistic.
    """
    return await statistic_service.bulk_create(dtos=statistics)


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_all_statistic() -> None:
    """
    Delete all statistic.
    """
    return await statistic_service.delete_all()
