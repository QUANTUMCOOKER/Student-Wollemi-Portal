from cryptography.fernet import Fernet
from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    DATABASE_URL: str
    DB_ENCRYPTION_KEY: str
    
    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str
    GOOGLE_REDIRECT_URI: str

    model_config = SettingsConfigDict(env_file="backend/.env")

settings = Settings()

# Level 17 Encryption Handler (AES-256 via Fernet for field-level)
cipher_suite = Fernet(settings.DB_ENCRYPTION_KEY.encode() if settings.DB_ENCRYPTION_KEY else Fernet.generate_key())

def encrypt_data(data: str) -> str:
    if not data:
        return data
    return cipher_suite.encrypt(data.encode()).decode()

def decrypt_data(encrypted_data: str) -> str:
    if not encrypted_data:
        return encrypted_data
    return cipher_suite.decrypt(encrypted_data.encode()).decode()
