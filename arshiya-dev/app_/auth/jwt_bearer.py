from fastapi import Request , HTTPException
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from auth.jwt_handler import decode_jwt

class jwt_auth(HTTPBearer):
    def __init__(self,auto_Error:bool=True):
        super(jwt_auth,self).__init__(auto_error=auto_Error)

    async def __call__(self,request:Request):
        credetials = HTTPAuthorizationCredentials=await super(jwt_auth,self).__call__(request)
        if credetials:
            if not credetials.scheme == "Bearer":
                raise HTTPException(status_code=401,detail="Invalid Token")
            return credetials.credentials
        else:
            raise HTTPException(status_code=401,detail="Invalid Token")
    
    def verify_token(self,token:str):
        isTokenValid : bool = False
        payload : dict = decode_jwt(token)
        if payload:
            isTokenValid = True
        return isTokenValid




