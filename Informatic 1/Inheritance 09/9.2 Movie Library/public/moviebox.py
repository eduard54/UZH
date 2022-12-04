#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from movie import Movie

class MovieBox(Movie):

    def __init__(self, title, movies):
        if len(title) == 0 or len(movies) == 0:
            raise Warning("one or two inputs empty")

        for movie in movies:
            if not isinstance(movie, Movie):
                raise Warning("Movie not in List")
        self.__title = title 
        self.__movies = movies

    def __eq__(self, other):
        if self.get_title() == other.get_title() and self.get_movies() == other.get_movies():
            return True
        else: 
            return False
    
    def __repr__(self):
        return f'MovieBox("{self.__title}", {self.__movies})'
    
    def __hash__(self):
        return hash(self.__title, tuple(self.__movies))

    def get_title(self):
        return self.__title

    def get_actors(self):
        actors = []
        for movie in self.__movies:
            actors.extend(movie.get_actors())
            actors = sorted(set(actors))
        return actors

    def get_duration(self):
        duration = 0
        for movie in self.__movies:
            duration += movie.get_duration()
        return duration

    def get_movies(self):
    	return self.__movies.copy()

a = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
z = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
d = MovieBox("Top Movies", [a, z])
y = MovieBox("Top Movies", [a])
print((d == y))
    # also implement the required special functions
