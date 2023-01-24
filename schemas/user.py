from typing import Optional
from pydantic import BaseModel

# Esto es muy parecido a struct en C
class User(BaseModel):  #BaseModel es un valor default
    id: Optional[str]
    name: str
    email: str
    password: str