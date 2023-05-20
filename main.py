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
    # Convert the input to V2 protocol
    v2_input = {
        "hf_pipeline": request.hf_pipeline,
        "inputs": request.inputs,
        "parameters": request.parameters,
    }

    # Send the input to the model
    response = await httpx.post(request.model_deployed_url, json=v2_input)
    response.raise_for_status()

    # Return the response from the model
    return response.json()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
