from src.database import database
from src.contact_form.models import contact_form
from src.contact_form.schemas import ContactForm


async def submit_contact_form(contact_form_data: ContactForm) -> None:
    insert_query = contact_form.insert().values(
        {
            "name": contact_form_data.name,
            "email": contact_form_data.email,
            "phone_number": contact_form_data.phone_number,
            "message": contact_form_data.message,
        }
    )

    await database.execute(insert_query)
