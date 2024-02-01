from fastapi import HTTPException, status, Security, FastAPI,Header,Depends
from fastapi.security import APIKeyHeader, APIKeyQuery
from typing import Annotated
# sign in to get api key and store the api key in the database with the username 
api_keys = [
    "anmar"
]

api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)


def get_api_key(
        a: str = Security(api_key_header)
) -> str:
    if a in api_keys:
        return a
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or missing API Key",
    )


app = FastAPI()


@app.get("/public")
def public():
    """A public endpoint that does not require any authentication."""
    return "Public Endpoint"


@app.get("/protecteeeeeeeeeeed")
async def read_items(user_agent: Annotated[str | None, Header()] = None):
    """A private endpoint that requires a valid API key to be provided."""
    return {"User-Agent": user_agent}

@app.get("/protected")
def private(api_key: str = Security(get_api_key)):
    """A private endpoint that requires a valid API key to be provided."""
    return f"Private Endpoint. API Key: {api_key}"


@app.get("/items/")
async def read_items(u:str=Depends(api_key_header)):
    return {"User-Agent": u}


