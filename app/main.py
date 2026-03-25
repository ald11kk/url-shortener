from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

from app.schemas import ShortenRequest, ShortenResponse
from app.shortener import create_short_url, get_original_url

app = FastAPI()

BASE_URL = "http://localhost:8000"

@app.post("/shorten", response_model=ShortenResponse)
def shorten_url(request: ShortenRequest) -> ShortenResponse:
    short_code = create_short_url(str(request.url))
    return ShortenResponse(short_code = short_code, short_url = f"{BASE_URL}/{short_code}")

@app.get("/{short_code}")
def redirect_to_long_url(short_code: str) -> RedirectResponse:
    long_url = get_original_url(short_code)
    if long_url:
        return RedirectResponse(long_url, status_code=301)
    else:
        raise HTTPException(status_code=404, detail="URL not found")
    
