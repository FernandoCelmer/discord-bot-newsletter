from json import dumps
from typing import List

from requests import request, Response
from pydantic import BaseModel
from configurations import Config


def is_ok(response: Response):
    return response.status_code in [200, 201]


class BaseAPI:

    RESOURCE = ''

    def __init__(self):
        self.config = Config()
        self.headers = {'Content-Type': 'application/json'}
        self.url = f"{self.config.api_url}/v1/{self.RESOURCE}"

    def _get(self, params: dict = {}):
        return request(
            method="GET",
            headers=self.headers,
            url=self.url,
            params=params,
        )

    def _post(self, payload: dict = {}):
        return request(
            method="POST",
            headers=self.headers,
            url=self.url,
            data=dumps(payload)
        )

    def _patch(self, id: str, payload: dict = {}):
        return request(
            method="PATCH",
            headers=self.headers,
            url=f"{self.url}/{id}",
            data=dumps(payload)
        )


class BaseResponse:

    def __init__(self, status_code: int, data: List):
        self.status_code = status_code
        self.data = data

    @staticmethod
    def schema(schema):
        def decorator(fun):
            def wrapper(*args, **kwargs):
                data = []
                response = fun(*args, **kwargs)
                if is_ok(response=response):
                    new_data = response.json()
                    if new_data:
                        if type(new_data) == list:
                            data = [schema(**item) for item in new_data]
                        else:
                            data.append(schema(**new_data))

                return BaseResponse(
                    status_code=response.status_code,
                    data=data
                )
            return wrapper
        return decorator
