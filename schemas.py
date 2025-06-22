from datetime import datetime
from pydantic import BaseModel


class SecurityEvent(BaseModel):
    event_type: str
    user_id: str
    ip_address: str
    status: str
    timestamp: datetime
