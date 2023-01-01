from pydantic import BaseModel
from types import NoneType

class IUrlTranslation(BaseModel):
    url: str
    token: str | NoneType = None

class IData(BaseModel):
    url_translation: IUrlTranslation

__all__ = [ IData, IUrlTranslation ]