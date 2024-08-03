# Third Party Library
from fastapi import APIRouter, Depends, Request, status, Query
from fastapi.responses import JSONResponse, StreamingResponse
from sqlalchemy.orm.session import Session
# Project Library
from pdf_generator.core.utils.util import process_form_data
from pdf_generator.core.utils.database import get_db
from pdf_generator.cruds.users import save_form
# Standard Library
import logging
import io


logger = logging.getLogger(__name__)

router = APIRouter()


@router.post('/')
async def create_form(
    request: Request,
    db: Session = Depends(get_db),
    output_type: str = Query("pdf", enum=["pdf", "json"])
):
    try:
        content_type = request.headers.get('Content-Type')

        if output_type not in ['pdf', 'json']:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={"status": False, "data": {}, "message": "Supported Output Types ['pdf', 'json']"}
            )
        
        if content_type and 'application/json' in content_type:
            json_body = await request.json()
            api_status, data, message, status_code = save_form(db, json_body)
        
        elif content_type and 'multipart/form-data' in content_type:
            form_data = await request.form()
            processed_data = process_form_data(form_data=form_data)
           
            api_status, data, message, status_code = save_form(db, processed_data)
        
        else:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={"status": False, "data": {}, "message": "Unsupported Content Type"}
            )
        
        # Return PDF as a streaming response if successful
        if api_status:
            if output_type == 'pdf':
                return StreamingResponse(
                    io.BytesIO(data[0]),
                    status_code=status.HTTP_201_CREATED,
                    media_type="application/pdf",
                    headers={"Content-Disposition": f"attachment; filename=filled_form{data[1].split('/')[-1]}"}
                )
            elif output_type == 'json':
                return JSONResponse(
                    status_code=status_code,
                    content={"status": api_status, "data": {"pdf_url": data[1]}, "message": message}
                )
        else:
            return JSONResponse(
                status_code=status_code,
                content={"status": api_status, "data": data, "message": message}
            )

    except Exception as e:
        logger.error(f"Error occurred: {e}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"status": False, "data": {}, "message": "Internal Server Error"}
        )