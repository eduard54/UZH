#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

class Movie:

    def __init__(self, title, actors, duration):
        if not title:
            raise Warning("empty title not allowed")

        if not (type(actors) == list and len(actors) != 0):
            raise Warning("wrong input")

        if duration < 1:
            raise Warning("Movie has to be longer than 1 minute")
        self.__title = title
        self.__actors = actors
        self.__duration = duration

    def __repr__(self):
        strMovie = f'Movie("{self.__title}", {self.__actors}, {self.__duration})'

        return strMovie.replace('\'', '"')

    def __eq__(self, other):
        if self.get_title() == other.get_title() and self.get_actors() == other.get_actors() and self.get_duration() == other.get_duration(): 
            return True
        else: 
            return False

    def __hash__(self):
        return hash(self.__title, tuple(self.__actors), self.__duration)

    def get_title(self):
        return self.__title

    def get_actors(self):
        return self.__actors.copy()

    def get_duration(self):
        return self.__duration

    # also implement the required special functions