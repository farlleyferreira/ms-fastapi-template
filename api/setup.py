import uvicorn
from project.routers import app

if __name__ == "__main__":
    uvicorn.run(
        "project:routers.app",
        host="0.0.0.0",
        reload=True,
        port=5000
    )
