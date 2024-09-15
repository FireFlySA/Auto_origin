from datetime import datetime
from typing import List

from pydantic import BaseModel, StrictStr, UUID4


class Books (BaseModel):
    isbn: str
    title: str
    subTitle: str
    author: str
    publish_date: datetime
    publisher:str
    pages: int
    description:str
    website: str


class UserRegisterResponse(BaseModel):
    userID: UUID4
    username: StrictStr
    books: List[Books]


class UserRegisterResponseError(BaseModel):
    code: int
    message: StrictStr



