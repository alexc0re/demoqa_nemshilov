import json
import logging as log
from pathlib import Path

import requests
from requests import utils

from support.headers import header
from support.logger import log_method





class DemoQaApi:
    log = log_method(logLevel=log.INFO)

    def __init__(self, base_url='https://demoqa.com'):
        self.base_url = base_url
        pass

    def api_request(self, method, endpoint, body='', headers=header):
        url = self.base_url + endpoint
        payload = json.dumps(body)
        session = requests.session()
        self.log.info(f'{method} at: {self.base_url}{endpoint}. Request body =  {body}, headers = {headers}')
        if method == "GET" or method == 'DELETE':
            response = session.request(method, url, headers=headers)
        else:
            response = session.request(method, url, headers=headers, data=payload)

        try:
            self.log.info(f'Response = {response.status_code} {response.json()}')
        except requests.exceptions.JSONDecodeError:
            self.log.info(f'Response = {response.status_code}, {response.text}')
            pass
        return response