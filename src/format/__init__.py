import json

IMG_WIDTH = 480
HEADER_N = 3


class Formatter:

    def __init__(self, book):
        self.book = book

    @property
    def authors(self):
        return ', '.join([self.author(a) for a in self.book.authors])

    def author(self, a):
        return a.name


class RstFormatter(Formatter):

    def format(self):
        return """
        `{title}`_
        {authors}
        {img}
        `{isbn}`_
        .. _`{title}`: {url}
        .. _`{isbn}`: {url}
        """.format(
                title=self.book.title,
                authors=self.authors,
                img=self.img,
                url=self.book.url,
                isbn=self.book.isbn.number
        )

    def author(self, author):
        return "`{name} <{url}>`".format(name=author.name, url=author.url)

    @property
    def img(self):
        return """
        .. image:: {url}
        :width: {w} px
        :alt: {alt}
        :align: center
        """.format(
                url=self.book.cover_m,
                w=IMG_WIDTH,
                alt=self.book.title)


class HtmlFormatter(Formatter):

    def format(self):
        return """
<p class="book">
    <a href="{url}">{title}</a><br>
    ISBN:<a href="{url}">{url}<a/><br>
    <img src="{image_url}" width="{w}"/>
</p>
        """.format(
                url=self.book.url,
                title=self.book.title,
                isbn=self.book.isbn.number,
                image_url=self.book.cover_m,
                authors=self.authors,
                w=IMG_WIDTH)

    def author(self, author):
        return '<a href="{url}" class="author">{name}</a>'.format(name=author.name, url=author.url)


class JsonFormatter:
    @staticmethod
    def format(book):
        return json.dumps(book.dic)
