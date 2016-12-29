from isbn.rest import Collection, Resource

def get_api():
    import falcon

    api = falcon.API()

    storage = {}

    isbn_collection = Collection(storage)
    isbn = Resource(storage)

    api.add_route('/isbns', isbn_collection)
    api.add_route('/isbns/{isbn}', isbn)
    return api

def main():
    from wsgiref import simple_server

    httpd = simple_server.make_server('127.0.0.1', 8000, get_api())
    httpd.serve_forever()

if __name__ == '__main__':
    main()
