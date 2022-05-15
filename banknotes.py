import string
from pydantic import BaseModel

class BankNote(BaseModel):
    scen1:string
    scen2:string