$.get('https://swapi-api.alx-tools.com/api/films/?format=json',
  function (data) {
    data.results.map(function (film) {
      return $('UL#list_movies').append('<li>' + film.title + '</li>');
    });
  });
