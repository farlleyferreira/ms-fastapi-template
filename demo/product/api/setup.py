import uvicorn
from project.routers import app
from project.infrastructure.environments.loader import Configs

startup = app
configs = Configs.get_by_key("api_configs")

if __name__ == "__main__":
    uvicorn.run(
        "setup:startup",
        host=configs["host"],
        reload=True,
        port=5000
    )
