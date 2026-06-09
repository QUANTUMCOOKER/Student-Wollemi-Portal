from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
import httpx
from app.core.config import settings
from app.core.security import create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.get("/google/login")
async def google_login():
    return {
        "url": f"https://accounts.google.com/o/oauth2/v2/auth?response_type=code&client_id={settings.GOOGLE_CLIENT_ID}&redirect_uri={settings.GOOGLE_REDIRECT_URI}&scope=openid%20profile%20email"
    }

@router.get("/google/callback")
async def google_callback(code: str):
    token_url = "https://oauth2.googleapis.com/token"
    data = {
        "code": code,
        "client_id": settings.GOOGLE_CLIENT_ID,
        "client_secret": settings.GOOGLE_CLIENT_SECRET,
        "redirect_uri": settings.GOOGLE_REDIRECT_URI,
        "grant_type": "authorization_code",
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(token_url, data=data)
        token_data = response.json()
        
        if "access_token" not in token_data:
            raise HTTPException(status_code=400, detail="Failed to retrieve access token from Google")
            
        user_info_url = "https://www.googleapis.com/oauth2/v3/userinfo"
        headers = {"Authorization": f"Bearer {token_data['access_token']}"}
        user_info_response = await client.get(user_info_url, headers=headers)
        user_info = user_info_response.json()
        
    # In a real app, you would check if the user exists in the DB or create them here.
    # For now, we return a JWT for the email retrieved.
    access_token = create_access_token(data={"sub": user_info["email"], "role": "student"})
    
    # Redirect back to frontend with token
    frontend_url = f"http://localhost:5173/auth-success?token={access_token}"
    return RedirectResponse(url=frontend_url)
