import uvicorn
from fastapi import FastAPI
from src.main.python.routers.ws import appTest
from src.main.python.routers.dataAccess import dataAccess
import asyncio


app = FastAPI(
    servers=[
        {"url": "http://host.docker.internal:10802/vscode-server/backend", "description": "internal"},
        {"url": "http://mydormroom.ddns.net:10802/vscode-server/backend", "description": "external"},
        {"url": "https://prod.example.com", "description": "production"},
    ],
    root_path="/api/v1",
)
app.include_router(appTest, prefix="")
app.include_router(dataAccess, prefix="/dataAccess")



if __name__ == '__main__':
    port = 8091
    workers = 2
    try:
        uvicorn.run("src.main.python.main:app", host="0.0.0.0", port=port, workers=workers, reload=True)
    except asyncio.CancelledError:
        pass
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Shutting down...")

        


