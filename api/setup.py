import uvicorn
from project.routers import app

startup = app

if __name__ == "__main__":
    uvicorn.run(
        "setup:startup",
        host="0.0.0.0",
        reload=True,
        port=5000
    )
