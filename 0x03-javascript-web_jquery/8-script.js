$.get('https://swapi-api.hbtn.io/api/films/?format=json', function(data) {
  $.each(data.results, function(list, movies) {
    $('#list_movies').append(`<li>${movies.title}</li>`)
  });
});