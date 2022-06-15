from pydantic import BaseModel


class AnalyzedTextEntity(BaseModel):
    char_type: int
    feature: tuple
    feature_raw: str
    is_unk: bool
    length: int
    posid: int
    rlength: int
    stat: int
    surface: str
    white_space: str
