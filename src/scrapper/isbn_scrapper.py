__author__ = 'carlos'

import urllib.request, json, socket, re

API_TEMPLATE = 'https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data'

FORMATS = ('rst', 'html')

class Isbn:

    KEY_TEMPLATE = 'ISBN:{isbn}'

    def __init__(self, number):
        self.number = number
        self.len = len(str(number))

    @property
    def ws_url(self):
        return API_TEMPLATE.format(isbn=self.number)

    @property
    def ws_key(self):
        return self.KEY_TEMPLATE.format(isbn=self.number)

    def request_book(self):
        request = urllib.request.Request(self.ws_url)
        with urllib.request.urlopen(request) as f:
            result = json.loads(f.read().decode('utf-8'))
        if result:
            return Book(self, result[self.ws_key])
        else:
            return None

    def __len__(self):
        return self.len


class Author:

    def __init__(self, data_dict):
        self.name = data_dict['name']
        self.url = data_dict['url']


class Book:

    def __init__(self, isbn, result):
        self.isbn = isbn
        self.title = result['title']
        self.url = result['url']
        self.number_of_pages = result['number_of_pages']
        if 'cover' in result:
            self.cover_s = result['cover']['small']
            self.cover_l = result['cover']['large']
            self.cover_m = result['cover']['medium']
        self.authors = []
        for a in result['authors']:
            self.authors.append(Author(a))

    def __str__(self):
        return u'{title}\n{isbn}\n{url}\n'.format(
                url=self.url,
                title=self.title,
                isbn=self.isbn.number)

    def __repr__(self):
        return self.__str__()

    @property
    def dic(self):
        return self.__dict__
