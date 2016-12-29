import json, socket, re, requests

__author__ = 'carlos'


class WsUrl:
    TEMPLATE = 'https://www.googleapis.com/customsearch/v1'
    QUERY_TEMPLATE = 'https://google.com?q={}'

FORMATS = ('rst', 'html')
API_KEY = 'AIzaSyDjSV54P5BpXojvY_5NPF-R9LkpRGk23WQ'
SEARCH_ENG_ID = '016672377533739393798:9mzqieqaeji'

DEFAULT_USER_IP = socket.gethostbyname(socket.gethostname())


class Isbn:
    def __init__(self, number):
        self.number = number
        self.len = len(str(number))


    @property
    def url_google_q(self):
        return WsUrl.QUERY_TEMPLATE.format(self.number)

    def request_book(self):
        result = requests.get('https://www.googleapis.com/customsearch/v1', params={'key': API_KEY, 'q': self.number, 'cx': SEARCH_ENG_ID})
        result = json.loads(result.text)
        result_img = requests.get('https://www.googleapis.com/customsearch/v1', params={'key': API_KEY, 'q': self.number, 'searchType': 'image', 'cx': SEARCH_ENG_ID})
        result_img = json.loads(result_img.text)
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
