from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_TITLE: str
    APP_DESCRIPTION: str
    APP_VERSION: str
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    FRONTEND_URL: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
