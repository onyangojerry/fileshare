from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
import jwt
import os
from dotenv import load_dotenv

load_dotenv()
router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """Simulated login: Normally, you should validate username & password."""
    user_data = {"sub": form_data.username}  # Replace with actual user verification
    access_token = create_access_token(user_data, timedelta(minutes=30))
    return {"access_token": access_token, "token_type": "bearer"}
