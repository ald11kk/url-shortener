from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

from app.schemas import shortenRequest, shortenResponse
from app.shortener import create_short_url, get_original_url

app = FastAPI()

BASE_URL = "http://localhost:8000/"

@app.post("/shorten", response_model=shortenResponse)
def shorten_url(request: shortenRequest):
    short_code = create_short_url(str(request.url))
    return shortenResponse(short_code = short_code, short_url = f"{BASE_URL}{short_code}")

@app.get("/{short_code}")
def redirect_to_long_url(short_code: str):
    long_url = get_original_url(short_code)
    if long_url:
        return RedirectResponse(long_url)
    else:
        raise HTTPException(status_code=404, detail="URL not found")
    
