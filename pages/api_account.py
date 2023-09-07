import pytest
from playwright.sync_api import expect

from base.demoqa_api import DemoQaApi



header =  {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}


class AccountAPI(DemoQaApi):


    def create_user(self):
        response = self.api_request(method='POST', endpoint='/Account/v1/User', body=self.body)
        userid = response.json()['userID']
        assert response.status_code == 201
        self.userid = userid


    def auth_user(self):
        response = self.api_request(method='GET', endpoint='/Account/v1/Authorized', body=self.body)
        assert response.status_code == 200, f"expexted code 200 , actual code: {response.status_code}"

    def generate_token(self):
        response = self.api_request(method='POST', endpoint='/Account/v1/GenerateToken', body=self.body)
        assert response.status_code == 200 , f"expexted code 200 , actual code: {response.status_code}"
        token = response.json()['token']
        self.header['Authorization'] = "Bearer " + token


    def get_user_info(self):
        response = self.api_request(method='GET', endpoint=f'/Account/v1/User/{self.userid}', headers=self.header)
        assert response.status_code == 200, f"expexted code 200 , actual code: {response.status_code}"

    @pytest.mark.xfail
    def delete_user(self):
        response = self.api_request(method='DELETE', endpoint=f'/Account/v1/User/{self.userid}', headers=self.header)
        assert response.status_code == 204 , f"expexted code 200 , actual code: {response.status_code}"


    def get_all_books(self):
        response = self.api_request(method='GET', endpoint='/BookStore/v1/Books')
        assert response.status_code == 200, f"expexted code 200 , actual code: {response.status_code}"

    def get_book_info(self):
        response = self.api_request(method='GET', endpoint='/BookStore/v1/Book?ISBN=9781449325862')
        assert response.status_code == 200 , f"expexted code 200 , actual code: {response.status_code}"


    def add_book_to_collection(self):
        payload = {
            "userId":self.userid ,
            "collectionOfIsbns": [
                {
                    "isbn": "9781449325862"
                }
            ]
        }
        response = self.api_request('POST', endpoint='/BookStore/v1/Books', headers=self.header,body=payload)
        assert response.status_code == 201 , f"expexted code 201 , actual code: {response.status_code}"

    def delete_books_from_collection(self):
        response = self.api_request('DELETE', endpoint=f'/BookStore/v1/Books/?UserId={self.userid}', headers=self.header)
        assert response.status_code == 204
