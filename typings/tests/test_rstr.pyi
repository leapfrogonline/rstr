from typing import AnyStr, Pattern
import unittest
import random

from rstr.rstr_base import Rstr


def assert_matches(pattern: Pattern[AnyStr], value: str) -> None:
    errmsg: str = '{} does not match {}'.format(value, pattern)
    ...


class TestRstr(unittest.TestCase):
    def setUp(self) -> None:
        self.rs = Rstr()

    def test_specific_length(self) -> None:
        ...

    def test_length_range(self) -> None:
        ...

    def test_custom_alphabet(self) -> None:
        ...

    def test_alphabet_as_list(self) -> None:
        ...

    def test_include(self) -> None:
        ...

    def test_include_specific_length(self) -> None:
        '''
        Verify including characters doesn't make the string longer than intended.
        '''
        ...

    def test_exclude(self) -> None:
        ...

    def test_include_as_list(self) -> None:
        ...

    def test_exclude_as_list(self) -> None:
        ...


class TestSystemRandom(TestRstr):
    def setUp(self) -> None:
        self.rs = Rstr(random.SystemRandom())


class TestDigits(unittest.TestCase):
    def setUp(self) -> None:
        self.rs = Rstr()

    def test_all_digits(self) -> None:
        ...

    def test_digits_include(self) -> None:
        ...

    def test_digits_exclude(self) -> None:
        ...


class TestNondigits(unittest.TestCase):
    def setUp(self) -> None:
        self.rs = Rstr()

    def test_nondigits(self) -> None:
        ...

    def test_nondigits_include(self) -> None:
        ...

    def test_nondigits_exclude(self) -> None:
        ...


class TestLetters(unittest.TestCase):
    def setUp(self) -> None:
        self.rs = Rstr()

    def test_letters(self) -> None:
        ...

    def test_letters_include(self) -> None:
        ...

    def test_letters_exclude(self) -> None:
        ...


class TestUnambiguous(unittest.TestCase):
    def setUp(self) -> None:
        self.rs = Rstr()

    def test_unambiguous(self) -> None:
        ...

    def test_unambiguous_include(self) -> None:
        ...

    def test_unambiguous_exclude(self) -> None:
        ...


class TestCustomAlphabets(unittest.TestCase):
    def test_alphabet_at_instantiation(self) -> None:
        rs = Rstr(vowels='AEIOU')
        ...

    def test_add_alphabet(self) -> None:
        rs = Rstr()
        ...


def main() -> None:
    ...


if __name__ == '__main__':
    ...
