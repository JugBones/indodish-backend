from fastapi import APIRouter, status

from src.contact_form import services
from src.contact_form.schemas import ContactForm

router = APIRouter(prefix="/contact-form", tags=["contact-form"])


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    description="Submit contact form",
)
async def submit_form(contact_form_data: ContactForm):
    await services.submit_contact_form(contact_form_data)
