__author__ = 'carlos'


import urllib.request, json, socket, re


class WsUrl:

    IMG_TEMPLATE='https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q={}&userip={}'
    TEMPLATE='https://ajax.googleapis.com/ajax/services/search/fe?v=1.0&q={}&userip={}'
    QUERY_TEMPLATE='https://google.com?q={}'


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

    def request_book(self, referer = DEFAULT_USER_IP):
        request = urllib.request.Request(self.url, None, {'Referer': referer})
        request_img = urllib.request.Request(self.url_img, None, {'Referer': referer})
        with urllib.request.urlopen(request) as f:
            result = json.loads(f.readall().decode('utf-8'))
        with urllib.request.urlopen(request_img) as f:
            result_img = json.loads(f.readall().decode('utf-8'))
        return Book(self, result, result_img)

    def __len__(self):
        return self.len


class Book:

    def __init__(self,isbn, result, result_img):
        self.isbn = isbn
        self.title, self.url = self.extract_data(result['responseData']['results'])
        self.img_url = self.extract_img_url(result_img['responseData']['results'])
        self.title = re.split(";|\-|\_|\|", self.title, 1)

    @staticmethod
    def extract_img_url(result_img):
        if len(result_img) > 0:
            return result_img[0]['url']
        return None

    @staticmethod
    def extract_data(result):
        if len(result) > 0:
            return result[0]['titleNoFormatting'], result[0]['url']
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
