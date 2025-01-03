from fastapi import APIRouter, HTTPException
from models import ModelInput, ModelOutput
from llm_model_predict import llm_model_predict

api_router = APIRouter()

@api_router.post("/predict", response_model=ModelOutput)
async def predict(data: ModelInput):
    try:
        output = await llm_model_predict(data)
        return ModelOutput(model_output=output, status='ok')
    except:
        raise HTTPException(
            status_code=500, 
            detail=str(
                f'Ошибка вводимых данных {data.model_input}. Проверьте формат и правильность вводимых данных.'))
