from pydantic import BaseModel, ConfigDict
from typing import Literal
from datetime import datetime


class QueryGoodsStockDto(BaseModel):
    model_config = ConfigDict(strict=True)  # type hint assert level: strict
    success: bool
    resultCode: Literal["200", "-1", "-2", "-99"]
    resultMessage: str
    resultException: str
    data: list
    timestamp: datetime
    trackingNo: str
