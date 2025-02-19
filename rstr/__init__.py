from rstr.rstr import Rstr
from rstr.rstr import SameCharacterError as SameCharacterError
from rstr.xeger import Xeger

_default_xeger = Xeger()
_default_rstr = Rstr()

rstr = _default_rstr.rstr
xeger = _default_xeger.xeger


# This allows convenience methods from rstr to be accessed at the package
# level, without requiring the user to instantiate an Rstr() object.
printable = _default_rstr.printable
letters = _default_rstr.letters
uppercase = _default_rstr.uppercase
lowercase = _default_rstr.lowercase
digits = _default_rstr.digits
punctuation = _default_rstr.punctuation
nondigits = _default_rstr.nondigits
nonletters = _default_rstr.nonletters
whitespace = _default_rstr.whitespace
nonwhitespace = _default_rstr.nonwhitespace
normal = _default_rstr.normal
word = _default_rstr.word
nonword = _default_rstr.nonword
unambiguous = _default_rstr.unambiguous
postalsafe = _default_rstr.postalsafe
urlsafe = _default_rstr.urlsafe
domainsafe = _default_rstr.domainsafe
