import logging
from enum import Enum
from json import JSONDecodeError

import requests
from dataclasses import dataclass
from typing import MutableMapping, Union, Dict


@dataclass(frozen=True)
class HttpClientResponse:
    status_code: int
    headers: MutableMapping[str, str]
    text: str
    json: Union[dict, list]

    @staticmethod
    def from_request_response(requests_response: requests.Response):
        json = {}
        if requests_response.text:
            try:
                json = requests_response.json()
            except JSONDecodeError as err:
                logging.error(f'Failed to parse response to JSON: {err}')
        return HttpClientResponse(
            status_code=requests_response.status_code,
            headers=requests_response.headers,
            text=requests_response.text,
            json=json
        )


class RequestMethod(Enum):
    GET = 'get'
    POST = 'post'
    PUT = 'put'
    DELETE = 'delete'


class BaseHttpClient:

    headers: Dict[str, str]

    def __init__(self, base_url: str):
        self.base_url = base_url
        self.headers = {}
        self.auth = None
        self.session = requests.Session()

    def close_session(self):
        self.session.close()

    @property
    def cookies(self):
        return self.session.cookies.get_dict()

    def get_cookie(self, name:str) -> str:
        for key, value in self.cookies.items():
            if key == name:
                return value
        raise ValueError(f'Cookie with name {name} not found')

    def set_cookie(self, name: str, value: str, domain: str) -> None:
        cookie = requests.cookies.create_cookie(name=name, value=value, domain=domain)
        self.session.cookies.set_cookie(cookie)

    def set_header(self, key: str, value: str) -> None:
        self.headers[key] = value

    def remove_header(self, key: str) -> None:
        del self.headers[key]

    def set_auth_token(self, token: str) -> None:
        self.set_header('authorization', f'Bearer {token}')

