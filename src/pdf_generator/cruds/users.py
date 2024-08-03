import logging
from datetime import datetime

from fastapi import status

from pdf_generator.core.utils.exceptions import PdfGeneratorException
from pdf_generator.schemas.users import UserCreate
from pdf_generator.core.queries.users import create_user
from pdf_generator.core.utils.pdf_manager import PdfGenerator
from pdf_generator.core.utils.util import generate_dict_data
from pdf_generator.configs.settings import PDF_TEMPLATE_PATH

logger = logging.getLogger(__name__)

pdf_generator = PdfGenerator(PDF_TEMPLATE_PATH)

def save_form(db, request):
    logger.info("Received form data: %s", request)
    try:
        name = request.get("name")
        date_str = request.get("date")
        address = request.get("address")
        check_box_activities = list(set([str(check).lower() for check in request.get("check_box_activities", [])]))
        radio_activities = str(request.get("radio_activities", "")).lower()

        if not name or not date_str or not address or not check_box_activities or not radio_activities:
            return False, {}, "All fields are required.", status.HTTP_400_BAD_REQUEST

        # Convert date_str to a Python date object
        try:
            date_obj = datetime.strptime(date_str, '%d/%m/%Y').date()
        except ValueError as e:
            return False, {}, f"Invalid date format. Expected dd/mm/yyyy.", status.HTTP_400_BAD_REQUEST

        if not (2012 <= int(date_obj.strftime('%Y')) <= 2025):
            return False, {}, f"Date should be between 2012 and 2025", status.HTTP_400_BAD_REQUEST

        # Create the user object and save it
        new_user = create_user(
            db, 
            UserCreate( 
                name=name, 
                date=date_obj, 
                address=address, 
                check_box_activities=check_box_activities,
                radio_activities=radio_activities
            )
        )

        dict_data = generate_dict_data(
                new_user,
                date_obj,
                check_box_activities,
                radio_activities
            )

        output_path = pdf_generator.fill_pdf(dict_data)
        if not output_path:
            return False, {}, "Failed to fill PDF.", status.HTTP_500_INTERNAL_SERVER_ERROR
        
        data_bytes = pdf_generator.read_pdf_as_bytes(output_path)
        
        output_path = output_path.replace('public', 'static')

        return True, [data_bytes,output_path], "Form Saved successfully.", status.HTTP_201_CREATED

    except Exception as err:
        logger.info(err)
        raise PdfGeneratorException(str(err))




