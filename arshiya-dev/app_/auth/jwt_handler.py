# this file is resposible for  signings , encoding ,decoding and returing jwt
import time
import jwt
from decouple import config


JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

# function returns generated token
def token_response(token:str):
    return {
        "access token": token
    }

# function used for siging the jwt  token
def sign_jwt(user_id:str):
    payload = {
        "user_id": user_id,
        "expiry": time.time() + 600
        }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)


def decode_jwt(token:str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithm=[JWT_ALGORITHM])
        return decode_token if decode_token["expires"] >= time.time() else None
    except:
        return {}

