#!/usr/bin/node


$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (movies) {
  for (const titles of movies.results) {
    const titles = $('<li></li>').text(movies.title);
    $('#list_movies').append(titles);
  }
});