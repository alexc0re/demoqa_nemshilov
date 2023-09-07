import pytest

@pytest.mark.login_positive
def test_login_with_correct_creds(book_store_app):
    book_store_app.login_book_store_app()
    book_store_app.check_login_completed()

@pytest.mark.login_negative
def test_login_with_wrong_creds(book_store_app):
    book_store_app.login_book_store_app_wrong_creds()

@pytest.mark.login_negative
def test_login_bookstore_no_username(book_store_app):
    book_store_app.login_book_store_no_username()

@pytest.mark.login_negative
def test_login_bookstore_no_password(book_store_app):
    book_store_app.login_book_store_no_password()

@pytest.mark.login_positive
def test_logout(book_store_app):
    book_store_app.login_book_store_app()
    book_store_app.check_logout()

@pytest.mark.login_negative
def test_registration_no_recaptcha(book_store_app):
    book_store_app.check_new_user_registration_no_recaptha()
