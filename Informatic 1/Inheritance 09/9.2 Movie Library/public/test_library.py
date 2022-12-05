#!/usr/bin/env python3
import unittest
from unittest import TestCase
from movie import Movie
from moviebox import MovieBox
from library import Library

class LibraryTest(TestCase):

    def test_repr_movie(self):
        actual = repr(Movie("T", ["A", "B"], 123))
        expected = 'Movie("T", ["A", "B"], 123)'
        self.assertEqual(expected, actual)

    def test_repr_moviebox(self):
        actual = repr(MovieBox("T", [Movie("T2", ["A", "B"], 234)]))
        expected = 'MovieBox("T", [Movie("T2", ["A", "B"], 234)])'
        self.assertEqual(expected, actual)

    def test_library(self):
        a = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
        b = Movie("The Godfather", ["Brando", "Pacino"], 175)
        c = Movie("12 Angry Men", ["Fonda", "Cobb"], 96)
        d = MovieBox("Top Movies", [b, c])
        l = Library()
        l.add_movie(a)
        l.add_movie(d)
        self.assertEqual(413, l.get_total_duration())

    def test_eq(self):
        a = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
        b = Movie("The Godfather", ["Brando", "Pacino"], 175)
        self.assertFalse(a == b)

    def test_eq2(self):
        a = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
        b = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
        self.assertTrue(a == b)

    def test_eq_moviebox(self):
        a = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
        b = Movie("The Godfather", ["Brando", "Pacino"], 175)
        c = Movie("12 Angry Men", ["Fonda", "Cobb"], 96)
        e = MovieBox("Top Movies2", [a, c])
        f = MovieBox("Top Movies2", [a, c])
        self.assertTrue(e == f)

    def test_eq_moviebox2(self):
        a = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
        b = Movie("The Godfather", ["Brando", "Pacino"], 175)
        c = Movie("12 Angry Men", ["Fonda", "Cobb"], 96)
        d = MovieBox("Top Movies", [b, c])
        e = MovieBox("Top Movies2", [a, c])
        self.assertFalse(d == e)

    def test_movie_init_title(self):
        with self.assertRaises(Warning):
            a = Movie("", ["Robbins", "Freeman"], 142)

    def test_movie_init_actors(self):
        with self.assertRaises(Warning):
            a = Movie("asdf", [], 142)

    def test_movie_init_duration(self):
        with self.assertRaises(Warning):
            a = Movie("asdf", ["Robbins", "Freeman"], "142")

    def test_moviebox_init_title(self):
        with self.assertRaises(Warning):
            a = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
            c = Movie("12 Angry Men", ["Fonda", "Cobb"], 96)
            e = MovieBox("", [a, c])

    def test_moviebox_init_movies(self):
        with self.assertRaises(Warning):
            a = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
            c = "moin"
            e = MovieBox("asdf", [a, c])

    def test_eq_moviebox(self):
        a = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
        c = Movie("12 Angry Men", ["Fonda", "Cobb", "Robbins", "Freeman"], 96)
        e = MovieBox("Top Movies", [a, c])
        actual = e.get_actors()
        expected = ["Cobb", "Fonda", "Freeman", "Robbins"]
        self.assertEqual(expected, actual)
    # This current test suite only contains very basic test cases. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
unittest.main()