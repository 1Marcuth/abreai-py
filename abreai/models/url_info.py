from pydantic import BaseModel

class IAttributes(BaseModel):
    shortenedUrl: str
    token: str
    url: str

class IData(BaseModel):
    id: str
    type: str
    attributes: IAttributes

class IUrlInfo(BaseModel):
    data: IData


__all__ = [ IUrlInfo ]