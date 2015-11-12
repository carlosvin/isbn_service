
from functools import reduce
from scrapper import isbn_scrapper
import json, re, falcon, io

"""
For now we'll only accept 13 digits isbns
In the future, when we receive 10 digits we will convert it
"""

CONTENT_TYPE = 'application/json'

MIN_10=999999999
MAX_10=9999999999
MIN_13=999999999999
MAX_13=9999999999999

RE_DIGIT = re.compile("\d+")


def validate_content_type(req, resp, params):
    if req.content_type != CONTENT_TYPE:
        raise falcon.HTTPBadRequest('Bad request', 'Content type {} not allowed, expected {}'.format(req.content_type, CONTENT_TYPE))


def get_valid_isbn(req, resp, params):
    isbn = get_isbn_input(req, params)
    if is_valid(isbn):
        params['isbn'] = isbn
    else:
        raise falcon.HTTPBadRequest('Bad request', 'Invalid ISBN {}'.format(isbn))


def get_isbn_input(req, params):
    if params and params['isbn']:
        return isbn_parse(params['isbn'])
    else:
        return isbn_parse(str(req.stream.read(32)))


def is_valid(isbn):
    return MIN_10 < isbn < MAX_10 or MIN_13 < isbn < MAX_13


def isbn_parse(text):
    return int(reduce(lambda a, b: a + b, filter(lambda c: c.isdigit(), re.findall(RE_DIGIT, text))))


class Collection(object):

    def __init__(self, storage):
        self.storage = storage

    @falcon.before(get_valid_isbn)
    def on_post(self, req, resp, isbn):
        book = isbn_scrapper.Isbn(isbn).request_book()
        if book:
            self.storage[isbn] = json.dumps(book.dic)
            resp.status = falcon.HTTP_201
            resp.location = '{}/{}'.format(req.path, isbn)
        else:
            resp.status = falcon.HTTP_500


class Resource(object):

    def __init__(self, storage):
        self.storage = storage

    @falcon.before(get_valid_isbn)
    def on_get(self, req, resp, isbn):
        resp.content_type = CONTENT_TYPE
        resp.body = self.storage[isbn]
