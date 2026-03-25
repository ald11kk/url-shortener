from pydantic import BaseModel, HttpUrl

class shortenRequest(BaseModel):
    url: HttpUrl

class shortenResponse(BaseModel):
    short_code: str
    short_url: str