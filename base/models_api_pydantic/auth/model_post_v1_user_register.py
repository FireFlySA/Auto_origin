from datetime import datetime
from typing import List

from pydantic import BaseModel, StrictStr, StrictInt, UUID4


class Books (BaseModel):
    isbn: StrictStr
    title: StrictStr
    subTitle: StrictStr
    author: StrictStr
    publish_date: datetime
    publisher:StrictStr
    pages: StrictInt
    description:StrictStr
    website: StrictStr


class UserRegisterResponse(BaseModel):
    userID: UUID4
    username: StrictStr
    books: List[Books]


class UserRegisterResponseError(BaseModel):
    code: StrictInt
    message: StrictStr



