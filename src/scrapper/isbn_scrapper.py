__author__ = 'carlos'

import urllib.request, json, socket, re


class WsUrl:
    IMG_TEMPLATE = 'https://www.googleapis.com/customsearch/v1?q={}&searchType=image'
    TEMPLATE = 'https://www.googleapis.com/customsearch/v1?q={}'
    QUERY_TEMPLATE = 'https://google.com?q={}'


FORMATS = ('rst', 'html')

DEFAULT_USER_IP = socket.gethostbyname(socket.gethostname())


class Isbn:
    def __init__(self, number):
        self.number = number
        self.len = len(str(number))

    @property
    def url_img(self):
        return WsUrl.IMG_TEMPLATE.format(self.number, DEFAULT_USER_IP)

    @property
    def url(self):
        return WsUrl.TEMPLATE.format(self.number, DEFAULT_USER_IP)

    @property
    def url_google_q(self):
        return WsUrl.QUERY_TEMPLATE.format(self.number)

    def request_book(self, referer=DEFAULT_USER_IP):
        request = urllib.request.Request(self.url, headers={'Referer': referer})
        request_img = urllib.request.Request(self.url_img, headers={'Referer': referer})
        with urllib.request.urlopen(request) as f:
            result = json.loads(f.read().decode('utf-8'))
        with urllib.request.urlopen(request_img) as f:
            result_img = json.loads(f.read().decode('utf-8'))
        return Book(self, result, result_img)

    def __len__(self):
        return self.len


class Book:

    def __init__(self, isbn, result, result_img):
        self.isbn = isbn
        tmp_title, self.url = self.extract_data(Book.get_response(result))
        self.img_url = self.extract_img_url(Book.get_response(result_img))
        self.title = re.split(";|\-|\_|\|", tmp_title, 1)

    @staticmethod
    def get_response(r) -> dict:
        if r and 'items' in r and len(r['items']) > 0:
            return r['items'][0]
        return None

    @staticmethod
    def extract_img_url(result_img) -> str:
        if result_img:
            return result_img['thumbnailLink']
        return None

    @staticmethod
    def extract_data(result) -> tuple:
        if result:
            return result['title'], result['displayLink']
        return None, None

    def __str__(self):
        return u'{}\n{}\n{}\n{}\n{}\n'.format(
            self.url,
            self.title,
            self.isbn.url_google_q,
            self.isbn.number,
            self.img_url,
        )

    def __repr__(self):
        return self.__str__()

    @property
    def dic(self):
        return {
            'isbn': self.isbn.number,
            'title': self.title,
            'url': self.url,
            'img_url': self.img_url
        }
