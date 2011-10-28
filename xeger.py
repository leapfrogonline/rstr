import re
import string
from random import choice, randint

class Xeger(object):

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
        categories = {
            'category_digit': lambda: self.digits(1),
            'category_not_digit': lambda: self.non_digits(1),
            "category_space": lambda: self.whitespace(1),
            "category_not_space": lambda: self.nonwhitespace(1),
            "category_word": lambda: self.word(1),
            "category_not_word": lambda: self.nonword(1),
                      }

        cases = {"literal": lambda x: unichr(x),
                 "at": lambda x: '',
                 "in": lambda x: self.handle_state(choice(x)),
                 "any": lambda x: self.printable(1),
                 "category": lambda x: categories[x](),
                 'branch': lambda x: self.handle_state(x),
                 "subpattern": lambda x: self.handle_state(x),
                 "integer": lambda x: self.handle_state(x),
                 'max_repeat': lambda x: self.repeat(*x),
                 None: lambda x: ''.join(self.handle_state(i) for i in choice(x))
                 }

        opcode = state[0]
        value = state[1]

        return cases[opcode](value)

    def repeat(self, start_range, end_range, value):
        result = []
        times = randint(start_range, end_range)
        for i in xrange(times):
            result.append(''.join(self.handle_state(i) for i in value))
        return ''.join(result)

    def get_opcode(self, opcode):
        try:
            int(opcode)
        except ValueError:
            pass
        else:
            opcode = "integer"
        return opcode
