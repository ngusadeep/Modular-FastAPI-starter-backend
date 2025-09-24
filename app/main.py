from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.modules.auth.routes import router as auth_router
from app.modules.user.routes import router as user_router
from app.core.config import settings

app = FastAPI(
    title=settings.APP_TITLE,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
)

# CORS (allow frontend localhost)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers with prefixes
app.include_router(auth_router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(user_router, prefix="/api/v1/users", tags=["Users"])
