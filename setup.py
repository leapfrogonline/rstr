from setuptools import setup

classifiers = [
 'Development Status :: 5 - Production/Stable',
 'Intended Audience :: Developers',
 'License :: OSI Approved :: BSD License',
 'Operating System :: OS Independent',
 'Programming Language :: Python :: 3.5',
 'Programming Language :: Python :: 3.6',
 'Programming Language :: Python :: 3.7',
 'Programming Language :: Python :: 3.8',
 'Topic :: Software Development :: Testing',
]

with open('./LICENSE.txt') as f:
    _license = f.read()

with open('./README.rst') as f:
    _readme = f.read()

setup(name='rstr',
      version='2.2.6',
      description=_readme,
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
      url='https://github.com/leapfrogonline/rstr',
      packages=['rstr', 'rstr.tests'],
      test_suite='rstr.tests.suite',
      )
