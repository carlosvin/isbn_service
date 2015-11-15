import 'package:polymer/polymer.dart';
import 'book_element.dart';
import 'dart:html';
import 'dart:convert';

/// Silence analyzer [BookElement]
main() async {
  loadData();
  await initPolymer();
}

void loadData() {
  var url = "http://localhost:8000/isbns";

  // call the fe server asynchronously
  var request = HttpRequest.getString(url).then(onDataLoaded);
}

// print the raw json response text from the server
void onDataLoaded(String responseText) {
  var jsonString = responseText;
  print(jsonString);
  Map parsedMap = JSON.decode(jsonString);
  BookElement book = querySelector('#book');

  book.color = parsedMap['title'];
}
