from typing import List
import databases
import logging
from fastapi import FastAPI, HTTPException

DATABASE_URL = "sqlite:///./my_database.db"
database = databases.Database(DATABASE_URL)

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#Connect to database on startup
@app.on_event("startup")
async def startup():
    await database.connect()

#Disconnect to database on shutdown
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/read/first-chunck", response_model=List)
async def read_first_chunk():
    logger.info("first-chunck endpoint was called")
    query = "SELECT * FROM my_table LIMIT 10"
    try:
        return await database.fetch_all(query=query)
    except Exception as e:
        logger.error(f"Error fetching the first chunk: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error") from e
