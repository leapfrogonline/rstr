import re
import unittest
import random

from rstr.rstr_base import Rstr, SameCharacterError


def assert_matches(pattern, value):
    errmsg = '{} does not match {}'.format(value, pattern)
    assert re.match(pattern, value), errmsg


class TestRstr(unittest.TestCase):
    def setUp(self):
        self.rs = Rstr()

    def test_specific_length(self):
        assert_matches('^A{5}$', self.rs.rstr('A', 5))

    def test_length_range(self):
        assert_matches('^A{11,20}$', self.rs.rstr('A', 11, 20))

    def test_end_range_no_start_range(self):
        assert_matches('^A{1,20}$', self.rs.rstr('A', end_range=20))

    def test_custom_alphabet(self):
        assert_matches('^A{1,10}$', self.rs.rstr('AA'))

    def test_alphabet_as_list(self):
        assert_matches('^A{1,10}$', self.rs.rstr(['A', 'A']))

    def test_include(self):
        assert_matches('^[ABC]*@[ABC]*$', self.rs.rstr('ABC', include='@'))

    def test_include_specific_length(self):
        '''
        Verify including characters doesn't make the string longer than intended.
        '''
        assert_matches('^[ABC@]{5}$', self.rs.rstr('ABC', 5, include='@'))

    def test_exclude(self):
        for _ in range(0, 100):
            assert 'C' not in self.rs.rstr('ABC', exclude='C')

    def test_include_as_list(self):
        assert_matches('^[ABC]*@[ABC]*$', self.rs.rstr('ABC', include=['@']))

    def test_exclude_as_list(self):
        for _ in range(0, 100):
            assert 'C' not in self.rs.rstr('ABC', exclude=['C'])

    def test_raise_exception_if_include_and_exclude_parameters_contain_same_character(self):
        with self.assertRaisesRegex(SameCharacterError, r"include and exclude parameters contain same character \(B\)"):
            self.rs.rstr('A', include='B', exclude='B')
            self.rs.rstr('A', include=['B'], exclude=['B'])
        with self.assertRaisesRegex(SameCharacterError, r"include and exclude parameters contain same characters \(., .\)"):
            self.rs.rstr('A', include='BC', exclude='BC')


class TestSystemRandom(TestRstr):
    def setUp(self):
        self.rs = Rstr(random.SystemRandom())


class TestDigits(unittest.TestCase):
    def setUp(self):
        self.rs = Rstr()

    def test_all_digits(self):
        assert_matches(r'^\d{1,10}$', self.rs.digits())

    def test_digits_include(self):
        assert_matches(r'^\d*@\d*$', self.rs.digits(include='@'))

    def test_digits_exclude(self):
        for _ in range(0, 100):
            assert '5' not in self.rs.digits(exclude='5')


class TestNondigits(unittest.TestCase):
    def setUp(self):
        self.rs = Rstr()

    def test_nondigits(self):
        assert_matches(r'^\D{1,10}$', self.rs.nondigits())

    def test_nondigits_include(self):
        assert_matches(r'^\D*@\D*$', self.rs.nondigits(include='@'))

    def test_nondigits_exclude(self):
        for _ in range(0, 100):
            assert 'A' not in self.rs.nondigits(exclude='A')


class TestLetters(unittest.TestCase):
    def setUp(self):
        self.rs = Rstr()

    def test_letters(self):
        assert_matches(r'^[a-zA-Z]{1,10}$', self.rs.letters())

    def test_letters_include(self):
        assert_matches(r'^[a-zA-Z]*@[a-zA-Z]*$', self.rs.letters(include='@'))

    def test_letters_exclude(self):
        for _ in range(0, 100):
            assert 'A' not in self.rs.letters(exclude='A')


class TestUnambiguous(unittest.TestCase):
    def setUp(self):
        self.rs = Rstr()

    def test_unambiguous(self):
        assert_matches('^[a-km-zA-HJ-NP-Z2-9]{1,10}$', self.rs.unambiguous())

    def test_unambiguous_include(self):
        assert_matches('^[a-km-zA-HJ-NP-Z2-9@]{1,10}$', self.rs.unambiguous(include='@'))

    def test_unambiguous_exclude(self):
        for _ in range(0, 100):
            assert 'A' not in self.rs.unambiguous(exclude='A')


class TestCustomAlphabets(unittest.TestCase):
    def test_alphabet_at_instantiation(self):
        rs = Rstr(vowels='AEIOU')
        assert_matches('^[AEIOU]{1,10}$', rs.vowels())

    def test_add_alphabet(self):
        rs = Rstr()
        rs.add_alphabet('evens', '02468')
        assert_matches('^[02468]{1,10}$', rs.evens())


def main():
    unittest.main()


if __name__ == '__main__':
    main()
