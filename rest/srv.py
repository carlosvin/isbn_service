import falcon

from rest import isbns


api = application = falcon.API()

ISBN_PATH_NAME = 'isbns'

isbns = isbns.Resource(ISBN_PATH_NAME)

api.add_route('/{}'.format(ISBN_PATH_NAME), isbns)

if __name__ == '__main__':
    from wsgiref import simple_server

    httpd = simple_server.make_server('127.0.0.1', 8000, api)
    httpd.serve_forever()