# -*- coding: utf8 -*-
#
# TP - test Platform
#

import os

from setuptools import setup, find_packages

# Meta information
version = open('VERSION').read().strip()
dirname = os.path.dirname(__file__)

# Save version and author to __meta__.py
path = os.path.join(dirname, 'tp', '__meta__.py')
data = '''# Automatically created. Please do not edit.
__version__ = u'%s'
__author__ = u'Sebastian Schaetz
''' % version
with open(path, 'wb') as F:
    F.write(data.encode())

setup(
    # Basic info
    name='tp',
    version=version,
    author='Sebastian Schaetz',
    author_email='seb.schaetz@gmail.com',
    url='---',
    description='Test Platform Project',
    long_description="Not Yet",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
    ],

    # Packages and depencies
    package_dir={'': 'tp'},
    packages=find_packages('tp'),
    install_requires=[
        'omegaconf',
    ],
    extras_require={
        'dev': [
            'pytest',
        ],
    },

    # Other configurations
    zip_safe=False,
    platforms='any',
)
