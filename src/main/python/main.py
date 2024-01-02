import uvicorn
from fastapi import FastAPI
from src.main.python.routers.ws import appTest
from src.main.python.routers.quanTrading import appQuant
import logging
import asyncio
logging.basicConfig(level=logging.DEBUG, filename='loger.log', format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI() # build Fast API application
app.include_router(appTest, prefix="/appTest")
app.include_router(appQuant, prefix="/appQuant")



if __name__ == '__main__':
    port = 8001
    workers = 2
    try:
        uvicorn.run("src.main.python.main:app", host="0.0.0.0", port=port, workers=workers, reload=True)
    except asyncio.CancelledError:
        pass
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Shutting down...")

        


