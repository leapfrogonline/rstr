from rstr.xeger import Xeger as Rstr
from rstr.rstr_base import SameCharacterError

_default_instance = Rstr()

rstr = _default_instance.rstr
xeger = _default_instance.xeger

# This allows convenience methods from rstr to be accessed at the package
# level, without requiring the user to instantiate an Rstr() object.
for alpha in _default_instance._alphabets.keys():
    globals()[alpha] = getattr(_default_instance, alpha)
