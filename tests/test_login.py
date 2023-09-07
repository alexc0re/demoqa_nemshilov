def test_login_with_correct_creds(book_store_app):
    book_store_app.login_book_store_app()
    book_store_app.check_login_completed()


def test_login_with_wrong_creds(book_store_app):
    book_store_app.login_book_store_app_wrong_creds()


def test_login_bookstore_no_username(book_store_app):
    book_store_app.login_book_store_no_username()


def test_login_bookstore_no_password(book_store_app):
    book_store_app.login_book_store_no_password()

def test_logout(book_store_app):
    book_store_app.login_book_store_app()
    book_store_app.check_logout()

def test_registration_no_recaptcha(book_store_app):
    book_store_app.check_new_user_registration_no_recaptha()
