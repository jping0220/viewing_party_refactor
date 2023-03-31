import pytest
from viewing_party.movie import Movie

def test_1():
    # Arrange
    movie = Movie("everything everywhere all at once", "Fiction", 5)
    # Act

    # Assert
    assert movie.name == "everything everywhere all at once"
    assert movie.genre == "Fiction"
    assert movie.rating == 5

def test_empty_movie_name():
    movie = Movie("", "Fiction", 5)
    assert movie.name == ""
    assert movie.genre == "Fiction"
    assert movie.rating == 5
