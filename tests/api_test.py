import pytest


@pytest.mark.api_flow
def test_api_create_user(account):
    account.create_user()


@pytest.mark.api_flow
def test_api_auth_user(account):
    account.auth_user()


@pytest.mark.api_flow
def test_api_generate_token(account):
    account.generate_token()


@pytest.mark.api_flow
def test_api_get_user_info(account):
    account.get_user_info()


@pytest.mark.api_flow
def test_api_get_all_books(account):
    account.get_all_books()


@pytest.mark.api_flow
def test_api_get_book_info(account):
    account.get_book_info()


@pytest.mark.api_flow
def test_api_add_book_to_collection(account):
    account.add_book_to_collection()


@pytest.mark.api_flow
def test_api_delete_books_from_collection(account):
    account.delete_books_from_collection()

@pytest.mark.xfail
@pytest.mark.api_flow
def test_delete_user(account):
    account.delete_user()
