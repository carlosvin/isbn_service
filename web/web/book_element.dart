@HtmlImport('book_element.html')
library book_element;

import 'package:web_components/web_components.dart' show HtmlImport;
import 'package:polymer/polymer.dart';

@PolymerRegister('book-element')
class BookElement extends PolymerElement {
  @reflectable
  String title = 'e';

  @reflectable
  String isbn;

  BookElement.created() : super.created();
}
