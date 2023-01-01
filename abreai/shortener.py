from pydantic import validate_arguments
import httpx

from .models.url_info import IUrlInfo
from .models.data import IData, IUrlTranslation

base_url = "https://abre.ai"

class AbreAiError(Exception): ...

class AbreAiUrlInfo:
    def __init__(self, url_info: IUrlInfo) -> None:
        self.__url_info = url_info

    def get_id(self):
        return self.__url_info.data.id
    
    def get_type(self):
        return self.__url_info.data.type
    
    def get_shortened_url(self):
        return self.__url_info.data.attributes.shortenedUrl
    
    def get_alias(self):
        return self.__url_info.data.attributes.token

    def get_original_url(self): 
        return self.__url_info.data.attributes.url
    
    def get_data(self): 
        url_info = self.__url_info

        return {
            "id": url_info.data.id,
            "type": url_info.data.type,
            "alias": url_info.data.attributes.token,
            "urls": {
                "original": url_info.data.attributes.url,
                "shorted": url_info.data.attributes.shortenedUrl
            }
        }

    def get_raw_data(self):
        return self.__url_info.dict()

class AbreAi:
    @validate_arguments
    def shorten(self, url: str, alias: str) -> AbreAiUrlInfo:
        request_url = f"{base_url}/_/generate"
        data = IData(
            url_translation = IUrlTranslation(
                url = url,
                token = alias
            ).dict()
        ).dict()

        response = httpx.post(request_url, json=data)

        if response.status_code == 400:
            data_response: dict = response.json()

            if "errors" in data_response.keys():
                if "token" in data_response["errors"].keys():
                    if "já existe" in data_response["errors"]["token"]:
                        raise AbreAiError("That url alias already exists, use another one and try again!")

            raise AbreAiError(response.text)

        if response.status_code != 201:
            raise AbreAiError(response.text)

        data_response = response.json()

        return AbreAiUrlInfo(IUrlInfo(**data_response))

__all__ = [ AbreAi ]