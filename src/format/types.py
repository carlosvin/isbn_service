import format

JSON = 'application/json'
HTML = 'text/html'
RST = 'application/rst'
NIKOLA = 'application/nikola'

FORMATTERS = {
    JSON: format.JsonFormatter(),
    HTML: format.HtmlFormatter(),
    RST: format.RstFormatter(),
    NIKOLA: format.BookNikolaFormatter(),
}

