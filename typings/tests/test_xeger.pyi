import unittest

from rstr.rstr_base import Rstr


class TestXeger(unittest.TestCase):
    def setUp(self) -> None:
        self.rs = Rstr()

    def test_literals(self) -> None:
        pattern = r'foo'
        ...

    def test_dot(self) -> None:
        '''
        Verify that the dot character doesn't produce newlines.
        See: https://bitbucket.org/leapfrogdevelopment/rstr/issue/1/
        '''
        pattern = r'.+'
        ...

    def test_digit(self) -> None:
        pattern = r'\d'
        ...

    def test_nondigits(self) -> None:
        pattern = r'\D'
        ...

    def test_literal_with_repeat(self) -> None:
        pattern = r'A{3}'
        ...

    def test_literal_with_range_repeat(self) -> None:
        pattern = r'A{2, 5}'
        ...

    def test_word(self) -> None:
        pattern = r'\w'
        ...

    def test_nonword(self) -> None:
        pattern = r'\W'
        ...

    def test_or(self) -> None:
        pattern = r'foo|bar'
        ...

    def test_or_with_subpattern(self) -> None:
        pattern = r'(foo|bar)'
        ...

    def test_range(self) -> None:
        pattern = r'[A-F]'
        ...

    def test_character_group(self) -> None:
        pattern = r'[ABC]'
        ...

    def test_carot(self) -> None:
        pattern = r'^foo'
        ...

    def test_dollarsign(self) -> None:
        pattern = r'foo$'
        ...

    def test_not_literal(self) -> None:
        pattern = r'[^a]'
        ...

    def test_negation_group(self) -> None:
        pattern = r'[^AEIOU]'
        ...

    def test_lookahead(self) -> None:
        pattern = r'foo(?=bar)'
        ...

    def test_lookbehind(self) -> None:
        pattern = r'(?<=foo)bar'
        ...

    def test_backreference(self) -> None:
        pattern = r'(foo|bar)baz\1'
        ...

    def test_zero_or_more_greedy(self) -> None:
        pattern = r'a*'
        ...

    def test_zero_or_more_non_greedy(self) -> None:
        pattern = r'a*?'
        ...
