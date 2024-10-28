from pydantic import BaseModel, EmailStr, constr
from datetime import date
from typing import Optional

class ContactBase(BaseModel):
    first_name: constr(min_length=1)
    last_name: constr(min_length=1)
    email: EmailStr
    phone: str
    bithday: date
    additional_info: Optional[str] = None

class ContactCreate(ContactBase):
    pass

class ContactUpdate(BaseModel):
    first_name: Optional[constr(min_length=1)]
    last_name: Optional[constr(min_length=1)]
    email: Optional[EmailStr]
    phone: Optional[str]
    bithday: Optional[date]
    additional_info: Optional[str] = None

class ContactInDB(ContactBase):
    id: int

    class Config:
        orm_mode = True