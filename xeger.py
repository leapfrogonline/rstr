import re
import string
from random import choice, randint
from itertools import chain

#The * and + characters in a regular expression
# match up to any number of repeats in theory,
#(and actually 65535 repeats in python) but you
#probably don't want that many repeats in your
#generated strings. This sets an upper-bound on
#repeats generated from + and * characters.
STAR_PLUS_LIMIT = 100

class Xeger(object):
    def __init__(self):
        super(Xeger, self).__init__()
        self._categories = {
        'category_digit': lambda: self._alphabets['digits'],
        'category_not_digit': lambda: self._alphabets['nondigits'],
        "category_space": lambda: self._alphabets['whitespace'],
        "category_not_space": lambda: self._alphabets['nonwhitespace'],
        "category_word": lambda: self._alphabets['word'],
        "category_not_word": lambda: self._alphabets['nonword'],
                  }

        self._cases = {"literal": lambda x: unichr(x),
             "not_literal": lambda x: choice(
                                string.printable.replace(unichr(x), '')),
             "at": lambda x: '',
             "in": lambda x: self.handle_in(x),
             "any": lambda x: self.printable(1),
             "range": lambda x: [unichr(i) for i in xrange(x[0], x[1]+1)],
             "category": lambda x: self._categories[x](),
             'branch': lambda x: ''.join(self.handle_state(i) for i in choice(x[1])),
             "subpattern": lambda x: ''.join(self.handle_state(i) for i in x[1]),
             #"integer": lambda x: ''.join(self.handle_state(i) for i in x),
             'max_repeat': lambda x: self.repeat(*x),
             'negate': lambda x: [False],
             #None: lambda x: ''.join(self.handle_state(i) for i in choice(x))
             }

    def xeger(self, string_or_regex):
        try:
            pattern = string_or_regex.pattern
        except AttributeError:
            pattern = string_or_regex

        parsed = re.sre_parse.parse(pattern)
        return self.build_string(parsed)

    def build_string(self, parsed):
        newstr = []
        for state in parsed:
            newstr.append(self.handle_state(state))
        return ''.join(newstr)

    def handle_state(self, state):
        opcode, value = state
        opcode = self.get_opcode(opcode)

        return self._cases[opcode](value)

    def handle_in(self, value):
        candidates = list(chain(*(self.handle_state(i) for
                                                     i in value)))
        if candidates[0] is False:
            candidates = set(string.printable).difference(candidates[1:])
            return choice(list(candidates))
        else:
            return choice(candidates)

    def repeat(self, start_range, end_range, value):
        result = []
        end_range = min((end_range, STAR_PLUS_LIMIT))
        times = randint(start_range, end_range)
        for i in xrange(times):
            result.append(''.join(self.handle_state(i) for i in value))
        return ''.join(result)

    def get_opcode(self, opcode):
        try:
            int(opcode)
        except (ValueError, TypeError):
            pass
        else:
            opcode = "integer"
        return opcode
