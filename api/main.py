from typing import List, Union
from fastapi import FastAPI

from api.domain.analyzed_text_entity import AnalyzedTextEntity
from api.domain.input_text_entity import InputTextEntity
from api.domain.text_analyzer import TextAnalyzer

app = FastAPI()


@app.get('/healthz/')
async def healthz():
    return {'status': 'UP'}


@app.post("/text/analyze/", response_model=List[AnalyzedTextEntity])
async def analyze_text(request: InputTextEntity):
    analyzer = TextAnalyzer()
    return analyzer.analyze(request)
