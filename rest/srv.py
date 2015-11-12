import falcon

from rest import isbns


api = application = falcon.API()

ISBN_PATH_NAME = 'isbns'

isbn_collection = isbns.Collection(ISBN_PATH_NAME)
isbn = isbns.Resource(ISBN_PATH_NAME)

api.add_route('/isbns', isbn_collection)
api.add_route('/isbns/{isbn}', isbn)

if __name__ == '__main__':
    from wsgiref import simple_server

    httpd = simple_server.make_server('127.0.0.1', 8000, api)
    httpd.serve_forever()