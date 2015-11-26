@HtmlImport('book_element.html')
library book_element;

import 'package:web_components/web_components.dart' show HtmlImport;
import 'package:polymer/polymer.dart';

@PolymerRegister('book-element')
class BookElement extends PolymerElement {
  @property String color = 'red';
  @property String isbn;

  BookElement.created() : super.created();
}
