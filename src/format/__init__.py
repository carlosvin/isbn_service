import json

IMG_WIDTH = 480
HEADER_N = 3


class RstFormatter:
    def format(self, book):
        return """
        `{}`_
        {}
        .. _`{}`: {}
        """.format(book.title, self.img(book), book.title, book.url)

    @staticmethod
    def img(book):
        return """
        .. image:: {}
        :width: {} px
        :alt: {}
        :align: center
        """.format(book.img_url, IMG_WIDTH, book.title)


class HtmlFormatter:
    @staticmethod
    def format(book):
        return """
<p class="book">
    <a href="{}">{}</a><br>
    ISBN:<a href="{}">{}<a/><br>
    <img src="{}" width="{}"/>
</p>
        """.format(book.url, book.title, book.url, book.isbn.number, book.img_url, IMG_WIDTH)


class BookNikolaFormatter:
    @staticmethod
    def format(book):
        return """
.. book_figure:: {}
    :class: book-figure
    :url: {}
    :isbn_{}: {}
    :image_url: {}
        """.format(book.title, book.url, len(book.isbn), book.isbn.number, book.img_url)


class JsonFormatter:
    @staticmethod
    def format(book):
        return json.dumps(book.dic)
