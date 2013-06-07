from setuptools import setup
import unittest

setup(name='rstr',
      version='2.1.1',
      description='Generate random strings in Python',
      author='Leapfrog Direct Response LLC',
      author_email='oss@leapfrogdevelopment.com',
      url='http://bitbucket.org/leapfrogdevelopment/rstr/overview',
      packages=['rstr'],
      test_suite='rstr.tests.suite',
     )
