import pytest
from playwright.sync_api import expect

from support.generator import generate_name
from base.demoqa_api import DemoQaApi


name = generate_name()
userid = str
token = str
custom_header =  {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}

body = {"userName": name, "password": "6e8h4VSn4v#Z%bd"}
class AccountAPI(DemoQaApi):

    def create_user(self):
        global userid
        response = self.api_request(method='POST', endpoint='/Account/v1/User', body=body)
        userid = response.json()['userID']
        assert response.status_code == 201
        print(userid)
        return userid


    def auth_user(self):
        response = self.api_request(method='GET', endpoint='/Account/v1/Authorized', body=body)
        assert response.status_code == 200, f"expexted code 200 , actual code: {response.status_code}"

    def generate_token(self):
        response = self.api_request(method='POST', endpoint='/Account/v1/GenerateToken', body=body)
        assert response.status_code == 200 , f"expexted code 200 , actual code: {response.status_code}"
        token = response.json()['token']
        custom_header['Authorization'] = "Bearer " + token
        return custom_header


    def get_user_info(self):
        global userid, custom_header
        response = self.api_request(method='GET', endpoint=f'/Account/v1/User/{userid}', body='',headers=custom_header)
        assert response.status_code == 200, f"expexted code 200 , actual code: {response.status_code}"

    def delete_user(self):
        global userid, custom_header
        response = self.api_request(method='DELETE', endpoint=f'/Account/v1/User/{userid}',body='', headers=custom_header)
        assert response.status_code == 204 , f"expexted code 200 , actual code: {response.status_code}"


    def get_all_books(self):
        response = self.api_request(method='GET', endpoint='/BookStore/v1/Books')
        assert response.status_code == 200

    def get_book_info(self):
        response = self.api_request(method='GET', endpoint='/BookStore/v1/Book?ISBN=9781449325862')
        assert response.status_code == 200


    def add_book_to_collection(self):
        global userid
        payload = {
            "userId":userid ,
            "collectionOfIsbns": [
                {
                    "isbn": "9781449325862"
                }
            ]
        }
        response = self.api_request('POST', endpoint='/BookStore/v1/Books', headers=custom_header,body=payload)
        assert response.status_code == 201

    def delete_books_from_collection(self):
        global userid
        response = self.api_request('DELETE', endpoint=f'/BookStore/v1/Books/?UserId={userid}', headers=custom_header)
        assert response.status_code == 204
