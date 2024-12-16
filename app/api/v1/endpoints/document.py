from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services import DocumentService
from app.schemas import DocumentResponse
from app.core import settings

router = APIRouter()
document_service = DocumentService()

@router.post("/analyze", response_model=DocumentResponse)
async def analyze_document(
    file: UploadFile = File(...)
):
    if not file.filename.endswith('.pdf'):
        raise HTTPException(
            status_code=400, 
            detail="Only PDF files are allowed"
        )
    
    content = await file.read()
    if len(content) > settings.MAX_UPLOAD_SIZE:
        raise HTTPException(
            status_code=400,
            detail=f"File size exceeds {settings.MAX_UPLOAD_SIZE} bytes"
        )
    
    result = await document_service.process_pdf(content, file.filename)
    
    if not result.success:
        raise HTTPException(status_code=500, detail=result.error)
    
    return result