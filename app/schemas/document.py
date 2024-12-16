from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DocumentResponse(BaseModel):
    file_name: str
    text_content: str
    processed_at: datetime
    success: bool
    error: Optional[str] = None