import format

JSON = 'application/json'
HTML = 'text/html'
RST = 'application/rst'

FORMATTERS = {
    JSON: format.JsonFormatter,
    HTML: format.HtmlFormatter,
    RST: format.RstFormatter,
}

