import time

from env_setup import *

from playwright.sync_api import expect

from base.demoqa_base import DemoQa
import os


class BookStore_app(DemoQa):

    def navigate_to_book_store_app(self):
        self.page.get_by_text('Book Store Application').click()
        expect(self.page.locator('.main-header')).to_contain_text('Book Store')

    def navigate_to_profile(self):
        self.page.get_by_text('Profile').click()
        expect(self.page.locator('.main-header')).to_contain_text('Profile')

    def login_book_store_app(self, login: str = self.name, password: str = os.getenv('BOOK_PASSWORD')):
        self.open_demoqa()
        self.navigate_to_book_store_app()
        self.page.locator('#login').click()
        self.page.locator('#userName').fill(login)
        self.page.locator('#password').fill(password)
        self.page.locator('#login').click()


    def login_book_store_app_wrong_creds(self):
        self.open_demoqa()
        self.login_book_store_app(password='11111111')
        expect(self.page.locator('#name')).to_contain_text('Invalid username or password')


    def login_book_store_no_username(self):
        self.open_demoqa()
        self.login_book_store_app(login="")
        expect(self.page.locator('.is-invalid.form-control')).to_be_visible()

    def login_book_store_no_password(self):
        self.open_demoqa()
        self.login_book_store_app(password="")
        expect(self.page.locator('.is-invalid.form-control')).to_be_visible()

    def check_login_completed(self):
        expect(self.page.locator('#userName-value')).to_have_text(os.environ['BOOK_LOGIN'])

    def check_logout(self):
        self.page.locator("#submit").click()
        expect(self.page.locator('#userForm')).to_contain_text('Login in Book Store')

    def check_open_bookstore(self):
        self.open_demoqa()
        self.navigate_to_book_store_app()


    def check_new_user_registration_no_recaptha(self):
        self.open_demoqa()
        self.navigate_to_book_store_app()
        self.page.locator('#login').click()
        self.page.locator('#newUser').click()
        self.page.fill('#firstname','test')
        self.page.fill('#lastname','test')
        self.page.fill('#userName','test')
        self.page.fill('#password','6e8h4VSn4v%')
        self.page.click('#register')
        expect(self.page.locator('#name')).to_contain_text('Please verify reCaptcha to register!')

    def check_find_books(self):
        self.page.fill('#searchBox', 'Learning JavaScript')
        expect(self.page.locator('.rt-tr-group').first).to_contain_text('Learning JavaScript')
        self.page.get_by_text('Learning JavaScript').click()


    def add_book_to_collection(self):
        self.page.get_by_text('Add To Your Collection').click()
        self.page.on("alert", lambda alert: alert.accept())


    def check_book_adding_collection_no_login(self):
        expect(self.page.get_by_text('Add To Your Collection')).not_to_be_visible()




    def check_book_added_to_collection(self):
        self.navigate_to_profile()
        expect(self.page.get_by_text('Learning JavaScript')).to_be_visible()

    def check_book_deleting(self):
        self.page.click('#delete-record-undefined')
        self.page.click("#closeSmallModal-ok")
        expect(self.page.get_by_text('Learning JavaScript')).not_to_be_visible()






