import time




def test_add_book_to_collection(book_store_app):
    book_store_app.login_book_store_app()
    book_store_app.check_find_books()
    book_store_app.add_book_to_collection()
    book_store_app.check_book_added_to_collection()
    book_store_app.check_book_deleting()


def test_add_to_collection_not_logged_in(book_store_app):
    book_store_app.open_demoqa()
    book_store_app.navigate_to_book_store_app()
    book_store_app.check_find_books()
    book_store_app.check_book_adding_collection_no_login()

