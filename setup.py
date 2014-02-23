#!/bin/python2.7
# -*- coding: utf-8 -*-
"""
Lucas Ou-Yang 2014 -- http://codelucas.com

Setup guide: http://guide.python-distribute.org/creation.html
python setup.py sdist bdist_wininst upload
"""
from __future__ import print_function

import os.path
import warnings
import sys
try:
    from setuptools import setup
    setuptools_available = True
except ImportError:
    from distutils.core import setup
    setuptools_available = False

"""
try:
    # This will create an exe that needs Microsoft Visual C++ 2008
    # Redistributable Package
    import py2exe
except ImportError:
    if len(sys.argv) >= 2 and sys.argv[1] == 'py2exe':
        print("Cannot import py2exe", file=sys.stderr)
        exit(1)

py2exe_options = {
    "bundle_files": 1,
    "compressed": 1,
    "optimize": 2,
    "dist_dir": '.',
    "dll_excludes": ['w9xpopen.exe'],
}

py2exe_console = [{
    "script": "./vsummarize/__main__.py",
    "dest_base": "vsummarize",
}]

py2exe_params = {
    'console': py2exe_console,
    'options': {"py2exe": py2exe_options},
    'zipfile': None
}

if len(sys.argv) >= 2 and sys.argv[1] == 'py2exe':
    params = py2exe_params
else:
    #files_spec = [
    #    ('etc/bash_completion.d', ['vsummarize.bash-completion']),
    #    ('share/doc/vsummarize', ['README.txt']),
    #    ('share/man/man1', ['vsummarize.1'])
    #]

    root = os.path.dirname(os.path.abspath(__file__))
    data_files = []

    #for dirname, files in files_spec:
    #    resfiles = []
    #    for fn in files:
    #        if not os.path.exists(fn):
    #            warnings.warn('Skipping file %s since it is not present.
    #                Type  make  to build all automatically generated files.' % fn)
    #        else:
    #            resfiles.append(fn)
    #    data_files.append((dirname, resfiles))

    params = {
        'data_files': data_files,
    }
    if setuptools_available:
        params['entry_points'] = {'console_scripts': ['vsummarize = vsummarize:main']}
    else:
        params['scripts'] = ['bin/vsummarize']
"""

# Get the version from youtube_dl/version.py without importing the package
exec(compile(open('vsummarize/version.py').read(),
             'vsummarize/version.py', 'exec'))
requires = [
    'argparse',
    'decorator',
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

