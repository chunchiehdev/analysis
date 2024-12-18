from datetime import datetime
from pathlib import Path
from markitdown import MarkItDown
from app.schemas import DocumentResponse
from app.core import settings

class DocumentService:
    def __init__(self):
        self.markitdown = MarkItDown()
        settings.UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    
    async def process_pdf(
        self, 
        file_content: bytes, 
        filename: str
    ) -> DocumentResponse:
        temp_file = settings.UPLOAD_DIR / f"{datetime.now().timestamp()}_{filename}"
        
        try:
            temp_file.write_bytes(file_content)
            
            result = self.markitdown.convert(str(temp_file))
            
            return DocumentResponse(
                file_name=filename,
                text_content=result.text_content,
                processed_at=datetime.now(),
                success=True
            )
        except Exception as e:
            return DocumentResponse(
                file_name=filename,
                text_content="",
                processed_at=datetime.now(),
                success=False,
                error=str(e)
            )
        finally:
            if temp_file.exists():
                temp_file.unlink()