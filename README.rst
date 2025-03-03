===============================
rstr = Random Strings in Python
===============================

.. image:: https://circleci.com/gh/leapfrogonline/rstr.svg?style=svg
    :target: https://circleci.com/gh/leapfrogonline/rstr

rstr is a helper module for easily generating random strings of various types.
It could be useful for fuzz testing, generating dummy data, or other
applications.

It has no dependencies outside the standard library.

Use
---

The basic method of rstr is ``rstr()``. At a minimum, it requires one argument,
an alphabet of characters from which to create a string.

::

    >>> import rstr
    >>> rstr.rstr('ABC')
    'AACAACCB'

By default, it will return a string between 1 and 10 characters in length. You
may specify an exact length by including it as a second argument:

::

    >>> rstr.rstr('ABC', 4)
    'ACBC'

You can also generate a range of lengths by adding two arguments. In the following
case, rstr will return a string with a randomly selected length between 5 and 10
characters.

::

    >>> rstr.rstr('ABC', 5, 10)
    'CBCCCABAA'

It's also possible to include particular characters in your string. This is useful
when testing a validator to make sure that certain characters are rejected.
Characters listed in the 'include' argument will *always* be present somewhere
in the resulting string.

::

    >>> rstr.rstr('ABC', include='&')
    'CA&A'

Conversely, you can exclude particular characters from the generated string. This is
helpful when starting with a pre-defined population of characters.

::

    >>> import string
    >>> rstr.rstr(string.digits, exclude='5')
    '8661442'

Note that any of the arguments that accept strings can also
accept lists or tuples of strings:

::

    >>> rstr.rstr(['A', 'B', 'C'], include = ['@'], exclude=('C',))
    'BAAABBA@BAA'

Other methods
-------------

The other methods provided by rstr, besides ``rstr()`` and ``xeger()``, are convenience
methods that can be called without arguments, and provide a pre-defined alphabet.
They accept the same arguments as ``rstr()`` for purposes of
specifying lengths and including or excluding particular characters.

letters()
    The characters provided by string.letters in the standard library.

uppercase()
    The characters provided by string.uppercase in the standard library.

lowercase()
    The characters provided by string.lowercase in the standard library.

printable()
    The characters provided by string.printable in the standard library.

punctuation()
    The characters provided by string.punctuation in the standard library.

nonwhitespace()
    The characters provided by string.printable in the standard library, except
    for those representing whitespace: tab, space, etc.

digits()
    The characters provided by string.digits in the standard library.

nondigits()
    The characters provided by the concatenation of string.letters and
    string.punctuation in the standard library.

nonletters()
    The characters provided by the concatenation of string.digits and
    string.punctuation in the standard library.

normal()
    Characters commonly accepted in text input, equivalent to string.digits +
    string.letters + ' ' (the space character).

unambiguous()
    The characters provided by the concatenation of string.digits and
    string.letters except characters which are similar: 1, l and I, etc.

postalsafe()
    Characters that are safe for use in postal addresses in the United States:
    upper- and lower-case letters, digits, spaces, and the punctuation marks period,
    hash (#), hyphen, and forward-slash.

urlsafe()
    Characters safe (unreserved) for use in URLs: letters, digits, hyphen, period, underscore,
    and tilde.

domainsafe()
    Characters that are allowed for use in hostnames, and consequently, in internet domains: letters,
    digits, and the hyphen.

Xeger
-----

Inspired by the Java library of the same name, the ``xeger()`` method allows users to
create a random string from a regular expression.

For example to generate a postal code that fits the Canadian format:

    >>> import rstr
    >>> rstr.xeger(r'[A-Z]\d[A-Z] \d[A-Z]\d')
    u'R6M 1W5'

xeger works fine with most simple regular expressions, but it doesn't support all
Python regular expression features.

Custom Alphabets
----------------

If you have custom alphabets of characters that you would like to use with a method
shortcut, you can specify them by keyword when instantiating an Rstr object:

    >>> from rstr import Rstr
    >>> rs = Rstr(vowels='AEIOU')
    >>> rs.vowels()
    'AEEUU'

You can also add an alphabet to an existing instance with the add_alphabet() method:

    >>> rs.add_alphabet('odds', '13579')
    >>> rs.odds()
    '339599519'

Examples
--------

You can combine rstr with Python's built-in string formatting to produce strings
that fit a variety of templates.

An email address:

::

    '{0}@{1}.{2}'.format(rstr.nonwhitespace(exclude='@'),
                         rstr.domainsafe(),
                         rstr.letters(3))

A URL:

::

    'http://{0}.{1}/{2}/?{3}'.format(rstr.domainsafe(),
                                    rstr.letters(3),
                                    rstr.urlsafe(),
                                    rstr.urlsafe())

A postal address:

::

    """{0} {1}
    {2} {3}
    {4}, {5} {6}
    """.format(rstr.letters(4, 8).title(),
               rstr.letters(4, 8).title(),
               rstr.digits(3, 5),
               rstr.letters(4, 10).title(),
               rstr.letters(4, 15).title(),
               rstr.uppercase(2),
               rstr.digits(5),
               )

.. _SystemRandom: https://docs.python.org/3/library/random.html#random.SystemRandom
