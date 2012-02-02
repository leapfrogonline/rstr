from rstr_base import default_instance

for alpha in default_instance._alphabets.keys():
    globals()[alpha] = getattr(default_instance, alpha)
