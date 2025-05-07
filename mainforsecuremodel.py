from secure_model import SentimentAnalyzer, RateLimiter, API_KEY, api_key_header
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel

app = FastAPI()
rate_limiter = RateLimiter(requests_per_minute=2)

def test_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(
            status_code=403, detail="Invalid API key")
    
    # Check rate limit corresponding to the input api key
    is_limited, _ = rate_limiter.is_rate_limited(api_key)
    # Check if returned boolean by is_rate_limited is True
    if is_limited:
        # Raise the http exception with status code
        raise HTTPException(status_code=429,
            detail="Rate limit exceeded. Please try again later."
        )
    return api_key

class SentimentRequest(BaseModel):
    text: str

@app.post("/predict")
def get_prediction(
    request: SentimentRequest,
    api_key: str = Depends(test_api_key)
):
    sentiment_model = SentimentAnalyzer("sentiment_model.joblib")
    result = sentiment_model(request.text)
    return {
        "text": request.text,
        "sentiment": result,
        "status": "success"
    }
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)