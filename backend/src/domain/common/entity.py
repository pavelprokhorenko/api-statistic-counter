from pydantic import BaseModel


class Entity(BaseModel):
    """
    Generic entity schema.
    """

    class Config:
        orm_mode = True
