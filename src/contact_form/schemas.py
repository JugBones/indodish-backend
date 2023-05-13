from pydantic import BaseModel, EmailStr


class ContactForm(BaseModel):
    name: str
    email: EmailStr
    phone_number: str
    message: str
