
IMG_WIDTH = 480
HEADER_N = 3

class RstFormatter:

    def __init__(self, book):
        self.book = book

    def __str__(self):
        return """
        `{}`_
        {}
        .. _`{}`: {}
        """.format(self.book.title, self.img, self.book.title, self.book.url)

    @property
    def img(self):
        return """
        .. image:: {}
   		:width: {} px
   		:alt: {}
   		:align: center
        """.format(self.book.img_url, IMG_WIDTH, self.book.title)

    def __repr__(self):
        return self.__str__()

class HtmlFormatter:

    def __init__(self, book):
        self.book = book

    def __str__(self):
        return """
        <p><a href="{}">{}</a><br>ISBN:<a href="{}">{}<a/><br><img src="{}" width="{}"/></p>
        """.format(self.book.url_google_q, self.book.isbn, self.book.title, self.img_url, IMG_WIDTH)

class BookNikolaFormatter:

    def __init__(self, book):
        self.book = book

    def __str__(self):
        return """
.. book_figure:: {}
    :class: book-figure
    :url: {}
    :isbn_{}: {}
    :image_url: {}
	""".format(self.book.title, self.book.url, len(self.book.isbn.number), self.book.isbn.number, self.book.img_url)