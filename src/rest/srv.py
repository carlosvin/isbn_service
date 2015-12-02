import falcon
from rest import isbns

api = application = falcon.API()

storage = {}

isbn_collection = isbns.Collection(storage)
isbn = isbns.Resource(storage)

api.add_route('/isbns', isbn_collection)
api.add_route('/isbns/{isbn}', isbn)

if __name__ == '__main__':
    from wsgiref import simple_server

    httpd = simple_server.make_server('127.0.0.1', 8000, api)
    httpd.serve_forever()
