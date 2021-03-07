import uvicorn
from project.routers import app
from project.infrastructure.environments.loader import Configs

configs = Configs.get_by_key("api_configs")

if __name__ == "__main__":
    uvicorn.run(
        "project:routers.app",
        host=configs["host"],
        reload=True,
        port=5000
    )
