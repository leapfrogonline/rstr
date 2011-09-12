import re
import unittest

from rstr import Rstr

class TestRstr(unittest.TestCase):
    def test_custom_alphabet(self):
        r = Rstr()
        assert re.match('^A{1,10}$', r.rstr('AA'))

    def test_alphabet_as_list(self):
        r = Rstr()
        assert re.match('^A{1,10}$', r.rstr(['A', 'A']))

    def test_include_as_list(self):
        r = Rstr()
        assert re.match('^[ABC]*@[ABC]*$', r.rstr('ABC', include=["@"]))

    def test_exclude_as_list(self):
        r = Rstr()
        for i in xrange(0, 100):
            assert 'C' not in r.rstr('ABC', exclude=['C'])

class TestDigits(unittest.TestCase):
    def test_all_digits(self):
        r = Rstr()
        assert re.match('^\d{1,10}$', r.digits())

    def test_digits_include(self):
        r = Rstr()
        assert re.match('^\d*@\d*$', r.digits(include='@'))

    def test_digits_exclude(self):
        r = Rstr()
        for i in xrange(0, 100):
            assert '5' not in r.digits(exclude='5')

class TestNondigits(unittest.TestCase):
    def test_nondigits(self):
        r = Rstr()
        assert re.match('^\D{1,10}$', r.nondigits())

    def test_nondigits_include(self):
        r = Rstr()
        assert re.match('^\D*@\D*$', r.nondigits(include='@'))

    def test_nondigits_exclude(self):
        r = Rstr()
        for i in xrange(0, 100):
            assert 'A' not in r.nondigits(exclude='A')

class TestLetters(unittest.TestCase):
    def test_letters(self):
        r = Rstr()
        assert re.match('^[a-zA-Z]{1,10}$', r.letters())

    def test_nondigits_include(self):
        r = Rstr()
        assert re.match('^[a-zA-Z]*@[a-zA-Z]*$', r.letters(include='@'))

    def test_nondigits_exclude(self):
        r = Rstr()
        for i in xrange(0, 100):
            assert 'A' not in r.letters(exclude='A')


if __name__ == '__main__':
    unittest.main()
