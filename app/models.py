from pydantic import BaseModel


class ModelInput(BaseModel):
    task: str = 'complition'
    reagents: str
    products: str = None
    

class ModelOutput(BaseModel):
    reagents: str
    products: str
    status: str

