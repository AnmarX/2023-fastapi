from fastapi import FastAPI, Depends
from typing import Optional

app = FastAPI()

# Define a dependency function with arguments
def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

# Use the dependency in a path operation
@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    # The `commons` parameter will receive the values returned by `common_parameters`
    # FastAPI automatically handles query parameters `q`, `skip`, and `limit`
    return commons

# Example with manual argument passing
@app.get("/manual_items/")
async def read_manual_items():
    # Manually calling the dependency function
    commons = common_parameters(q="manual", skip=1, limit=50)
    return commons