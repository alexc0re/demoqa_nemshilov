

def test_api_flow(account):
    account.create_user()
    account.auth_user()
    account.generate_token()
    account.get_user_info()
    account.get_all_books()
    account.get_book_info()
    account.add_book_to_collection()
    account.delete_books_from_collection()
    account.delete_user()




