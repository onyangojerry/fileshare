from fastapi import FastAPI
from app.routes import auth, files, admin

app = FastAPI(title="Distributed File Storage System")

# Register API routes
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(files.router, prefix="/files", tags=["File Storage"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])

@app.get("/")
def health_check():
    return {"message": "Distributed File Storage System is running!"}
