from pydantic import BaseModel, Field
from datetime import datetime, timedelta, timezone


class AccessTokenPayload(BaseModel):
    sub: int
    type: str = "access"
    iat: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    exp: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc) + timedelta(minutes=1)
    )