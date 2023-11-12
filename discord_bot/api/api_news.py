from typing import List
from configurations import Config

from api.schema import SchemaNews
from api.base import BaseAPI, BaseResponse



class ApiNews(BaseAPI):

    RESOURCE = 'news'

    @BaseResponse.schema(schema=SchemaNews)
    def get(self, scheduled: str) -> List[SchemaNews]:
        return self._get(
            params={"scheduled": scheduled}
        )
