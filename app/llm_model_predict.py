#from vllm import VLLM
from typing import Union, List
from models import ModelInput
import re

#TODO Подбор модели и промпт к ней для формата задачи
#model = VLLM('model_path')

async def llm_model_predict(model_input: ModelInput) -> Union[str, List[int]]:
    if model_input.task == 'complition':
        pass
        #str_input = preprocessing_complition(model_input.reagents)
    elif model_input.task == 'coefficients':
        pass
        #str_input = preprocessing_coefficients(model_input.reagents, model_input.products)
        
    response = model_input.reagents #model.generate(model_input)
    return response

def preprocessing_complition(chem_reaction: str) -> str:
    return ' '.join(re.findall('\S+', chem_reaction))

def preprocessing_coefficients(reagents: str, products: str) -> str:
    pass