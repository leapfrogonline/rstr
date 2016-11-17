from setuptools import setup

classifiers = [
 'Development Status :: 5 - Production/Stable',
 'Intended Audience :: Developers',
 'License :: OSI Approved :: BSD License',
 'Operating System :: OS Independent',
 'Programming Language :: Python :: 2.6',
 'Programming Language :: Python :: 2.7',
 'Programming Language :: Python :: 3.3',
 'Programming Language :: Python :: 3.4',
 'Programming Language :: Python :: 3.5',
 'Topic :: Software Development :: Testing',
]

with open('./LICENSE.txt') as f:
    _license = f.read()

setup(name='rstr',
      version='2.2.5',
      description='Generate random strings in Python',
      author='Leapfrog Direct Response LLC',
      author_email='oss@leapfrogdevelopment.com',
      maintainer='Brendan.McCollam',
      maintainer_email='brendan@mccoll.am',
      license=_license,
      classifiers=classifiers,
      keywords=['Random strings',
                'random',
                'strings',
                'reverse regular expression'],
      url='http://bitbucket.org/leapfrogdevelopment/rstr/overview',
      packages=['rstr', 'rstr.tests'],
      test_suite='rstr.tests.suite',
      )
