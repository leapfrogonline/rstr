import re
import unittest

from rstr import Xeger

MATCH_PATTERNS = [
    r'foo',
    r'\d',
    r'\D',
    r'A{3}',
    r'A{2,5}',
    r'\w',
    r'\W',
    r'foo|bar',
    r'(foo|bar)',
    r'[A-F]',
    r'[ABC]',
    r'^foo',
    r'foo$',
    r'[^a]',
    r'[^AEIOU]',
    r'foo(?=bar)',
    r'(foo|bar)baz\1',
    r'a*',
    r'a*?',
    r'\d{105}',
    r'\d{102,105}',
]

SEARCH_PATTERNS = [
    r'(?<=foo)bar',
]

REPEATED_MATCH_CASES = [
    (r'.+', None),
    (r'a*', 100),
    (r'b+', 100),
]


class TestXeger(unittest.TestCase):
    def setUp(self) -> None:
        self.rs = Xeger()

    def test_patterns_match(self) -> None:
        for pattern in MATCH_PATTERNS:
            with self.subTest(pattern=pattern):
                self.assertIsNotNone(re.match(pattern, self.rs.xeger(pattern)))

    def test_patterns_match_repeatedly(self) -> None:
        for pattern, max_length in REPEATED_MATCH_CASES:
            with self.subTest(pattern=pattern):
                for _ in range(100):
                    result = self.rs.xeger(pattern)
                    if max_length is not None:
                        self.assertLessEqual(len(result), max_length)
                    self.assertIsNotNone(re.match(pattern, result))

    def test_patterns_search(self) -> None:
        for pattern in SEARCH_PATTERNS:
            with self.subTest(pattern=pattern):
                self.assertIsNotNone(re.search(pattern, self.rs.xeger(pattern)))
