import unittest
import test_rstr
import test_xeger

def suite():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(test_rstr)
    suite.addTests(loader.loadTestsFromModule(test_xeger))
    return suite
