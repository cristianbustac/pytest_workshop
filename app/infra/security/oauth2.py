from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi.param_functions import Form

class OAuth2EmailRequestForm(OAuth2PasswordRequestForm):
    def __init__(self,email:str= Form(...),password:str=Form(...)):
        super().__init__(username=email, password=password,scope="")
        self.email = self.username