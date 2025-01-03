from pydantic import BaseModel


class ModelInput(BaseModel):
    task: str = 'complition'
    model_input: str = None
    

class ModelOutput(BaseModel):
    model_output: str
    status: str

