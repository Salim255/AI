from pydantic import BaseModel

class User(BaseModel):
    fullName: str
    age: int
    city: str