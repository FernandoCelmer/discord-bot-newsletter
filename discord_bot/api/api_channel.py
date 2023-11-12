from typing import List
from configurations import Config

from api.schema import SchemaChannel
from api.base import BaseAPI, BaseResponse, is_ok



class ApiChannel(BaseAPI):

    RESOURCE = 'channel'

    @BaseResponse.schema(schema=SchemaChannel)
    def get(self, code: str) -> List[SchemaChannel]:
        return self._get(
            params={"code": code}
        )

    @BaseResponse.schema(schema=SchemaChannel)
    def post(self, name: str, code: str) -> List[SchemaChannel]:
        return self._post(
            payload={
                "name": name,
                "code": code,
                "status": True
            }
        )

    @BaseResponse.schema(schema=SchemaChannel)
    def patch(self, code: str, status: bool = False) -> List[SchemaChannel]:
        response = self.get(code=code)

        if is_ok(response=response) and response.data:
            return self._patch(
                id=response.data[0].id,
                payload={"status": status}
            )

        return BaseResponse(
            status=False,
            status_code=404,
        )
