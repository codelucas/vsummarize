#!/bin/python2.7
# -*- coding: utf-8 -*-
"""
Lucas Ou-Yang 2014 -- http://codelucas.com

Setup guide: http://guide.python-distribute.org/creation.html
python setup.py sdist bdist_wininst upload
"""
try:
    from setuptools import setup
    setuptools_available = True
except ImportError:
    from distutils.core import setup
    setuptools_available = False

# Get the version from youtube_dl/version.py without importing the package
exec(compile(open('vsummarize/version.py').read(),
             'vsummarize/version.py', 'exec'))

requires = [
    'gdata',
    'moviepy',
    'numpy',
    'youtube-dl'
]

setup(
    name='vsummarize',
    version=__version__,
    description='Python video summarization.',
    long_description='',
    author='Lucas Ou-Yang',
    author_email='lucasyangpersonal@gmail.com',
    url='https://github.com/codelucas/vsummarize',
    packages=['vsummarize'],
    include_package_data=True,
    install_requires=requires,
    license="",
    zip_safe=False
    # **params
)
