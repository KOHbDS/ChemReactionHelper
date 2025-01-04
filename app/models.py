from pydantic import BaseModel
from typing import List, Optional


class ModelInput(BaseModel):
    task: str = 'complition'
    reagents: List[str]
    products: Optional[List[str]] = None
    

class ModelOutput(BaseModel):
    reagents: List[str]
    products: List[str]
    status: str

