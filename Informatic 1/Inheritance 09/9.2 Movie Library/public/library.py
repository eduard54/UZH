#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from movie import Movie
from moviebox import MovieBox

class Library(MovieBox):

    def __init__(self):
        self.__movies = []

    def add_movie(self, movie):
        if not (movie in self.__movies):
            self.__movies.append(movie)

    def get_movies(self):
        # I will use a dictionary to make sorting of the movies easier afterwards
        movie_dictionary = {}
        movie_list = []

        # Loop over all movies and moviesboxes in the library
        for movie in self.__movies:
            # Dependent on the type, use a different method to get the movies
            if isinstance(movie, MovieBox): 
                for moviebox_movie in movie.get_movies():
                    movie_dictionary[moviebox_movie.get_title()] = moviebox_movie
            else: movie_dictionary[movie.get_title()] = movie

        # Extract the movies from the dictionary, ordered by title
        for title in sorted(movie_dictionary):
            movie_list.append(movie_dictionary[title])
        return movie_list

    def get_total_duration(self):
        duration = 0
        for movie in self.__movies:
            duration += movie.get_duration()
        return duration