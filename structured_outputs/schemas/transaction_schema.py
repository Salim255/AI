from pydantic import BaseModel
from typing import Literal 
#Literal in Python and enum in JS/TS both: 
# allow you to define a variable that can only take on a specific
# set of values. In Python, you can use Literal from the typing module 
# to specify that a variable can only be one of a predefined set of values. 
# In JavaScript/TypeScript, you can use an enum to achieve a similar result by defining a set of named constants.

class Transaction(BaseModel):
    id: str
    amount: float
    currency: Literal["EUR", "USD", "GBP"]
    status: Literal['pending', 'completed', 'failed']
    timestamp: str