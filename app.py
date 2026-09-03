from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import ml_engine

# Initialize our FastAPI app
app = FastAPI()

# Allow our frontend webpage to safely talk to our backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define what data we expect from the webpage
class BiometricPayload(BaseModel):
    typing_speed: float
    mouse_speed: float
    error_rate: float

# Create a simple "Home" route to check if the server is alive
@app.get("/")
def home():
    return {"status": "Razorpay AI Fraud Shield Backend is running!"}

# Create the "Verify" route where the webpage sends data to the AI brain
@app.post("/verify")
def verify_user(payload: BiometricPayload):
    try:
        # Send the biometrics to our ml_engine.py brain
        result = ml_engine.analyze_biometrics(
            typing_speed=payload.typing_speed,
            mouse_speed=payload.mouse_speed,
            error_rate=payload.error_rate
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))