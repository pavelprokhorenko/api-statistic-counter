from sqlalchemy import TextClause, text


def generate_order_by_fields(order_by: list[str]) -> list[TextClause]:
    """
    Convert ordering fields like ["-name", "id"] to ["name desc", "id"].
    """

    ordering = [
        text(field) if not field.startswith("-") else text(f"{field[1:]} DESC")
        for field in order_by
    ]
    return ordering
