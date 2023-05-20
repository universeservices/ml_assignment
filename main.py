import json
import httpx
from pydantic import BaseModel, Field
from fastapi import FastAPI
from typing import Dict, Any, Optional

app = FastAPI()


class PredictRequest(BaseModel):
    hf_pipeline: str
    model_deployed_url: str
    inputs: str
    parameters: Dict[str, Any] = Field(default_factory=dict)


@app.post(path="/predict")
async def predict(request: PredictRequest):
    # Write your code here to translate input into V2 protocol and send it to model_deployed_url
    return {}
