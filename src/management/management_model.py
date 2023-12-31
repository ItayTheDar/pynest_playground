from pydantic import BaseModel


class Management(BaseModel):
    name: str
    age: int
