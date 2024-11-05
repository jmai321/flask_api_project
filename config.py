# config.py
class Config:
    SECRET_KEY = 'your_secret_key_here'
    JWT_SECRET_KEY = 'your_jwt_secret_key_here'
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5 MB limit for file uploads
