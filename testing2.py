import requests
import secrets
from passlib.hash import bcrypt
from passlib.context import CryptContext

r=requests.get("http://localhost:8888/protected",headers={"x-api-key":"anmar"})
print(r.status_code)

print(r.json())
print(r.text)


# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)


# def hash_the_password(password):
#     return pwd_context.hash(password)



# def generate_api_key():
#     return secrets.token_urlsafe(64)

# print(generate_api_key())
# print(hash_the_password(generate_api_key()))