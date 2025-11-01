from fastapi import Body, FastAPI

app = FastAPI()


@app.get('/books')
def get_books():
    """Returns books."""
    print('The earliest one')
    return [
        {
            'name': 'Param',
            'isbn': 1234,
        },
        {
            'name': 'LLD',
            'isbn': 1234,
        },
        {
            'name': 'HLD',
            'isbn': 1234,
        },
    ]


@app.get('/books')
async def get_books_async_same_url():
    """Returns books."""
    print('The latest one')
    return [
        {
            'name': 'Param',
            'isbn': 1234,
        },
        {
            'name': 'LLD',
            'isbn': 1234,
        },
        {
            'name': 'HLD',
            'isbn': 1234,
        },
    ]


@app.get('/async/books')
async def get_books_async():
    """Returns books."""
    print('The url with async')
    return [
        {
            'name': 'Param',
            'isbn': 1234,
        },
        {
            'name': 'LLD',
            'isbn': 1234,
        },
        {
            'name': 'HLD',
            'isbn': 1234,
        },
    ]


@app.get('/books/')
def get_query_param(some_query_param: str):
    """Gets query param.

    NOTE: You need to add `/` as there is an already defined url with `/books` for
    `get_books_async_url`.
    """
    return {
        'query_param': some_query_param,
    }


@app.get('/books/{some_param}/')
def get_with_path_and_query_param(some_param: str, query_param: str):
    """Tests path with query param."""
    return {
        'path_param': some_param,
        'query_param': query_param,
    }


@app.get('/books/{param1}/something/{param2}')  # Path parameters
def get_dynamic_param(param1: str, param2: int):
    """Gets multiple dynamic params.

    - Tests multiple param passing.
    - Param1 is returned as string.
    - Param2 is returned as an int.
    """
    return {
        'param1': param1,
        'param2': param2,
    }


# =================================================================================
# NOTE: Doing the following will always result in the second end-point being triggered
# with query param. To avoid this add a `/` in the second one.


# @app.post('/books')
# def create_book():
#     """Creates a book."""
#     return {'created_book': 'This is the created book'}


# @app.post('/books')  # Add `/` and check
# def create_given_book(book):
#     """Creates a book."""
#     return {'created_book': f'This is the created book {book}'}


# =================================================================================


@app.post('/books')  # Add `/` and check
def create_given_book(book=Body()):
    """Creates a book."""
    return {'created_book': f'This is the created book {book}'}


@app.put('/books/{book_id}')
def updates_the_book(book_id, data=Body()):
    """Performs put operation."""
    return {
        'book_id': book_id,
        'data': data,
    }


@app.delete('/books/{book_id}')
def delete_a_book(book_id):
    """Books"""
    return {'msg': f'Deleted book with ID: {book_id}'}
