import 'package:polymer/polymer.dart';
import 'book_element.dart';
import 'dart:html';
import 'dart:convert';

/// Silence analyzer [BookElement]
main() async {
  await initPolymer();
  loadData();
}

void loadData() {
  var url = "http://localhost/isbns";

  querySelector('#info').text = url;

  // call the fe server asynchronously
  var request = HttpRequest.getString(url)
      .then(onDataLoaded)
      .catchError((e) {
           querySelector('#info').text = "Got error: ${e.error}";
      }
  );
}

// print the raw json response text from the server
void onDataLoaded(String responseText) {
  querySelector('#info').text = responseText;

  Map parsedMap = JSON.decode(responseText);
  //BookElement book = (BookElement)querySelector('#book');
  //book.color = parsedMap['title'];

}
