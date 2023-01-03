from setuptools import setup, find_packages
import os

with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md')) as f:
    long_description = f.read()

setup(
    name='CreditCardComparison',
    version='0.0.0',
    description='CreditCardComparison --- A codebase to compare credit card benefits based on transactions.',
    long_description=long_description,
    url='https://github.com/suetAndTie/CreditCardComparison',
    author='suetAndTie',
    classifiers=[
        'Development Status :: 1 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Credit Cards' 'Programming Language :: Python :: 3.7',
    ],
    keywords='creditcard',
    packages=find_packages(where='src', exclude=['test']),
    package_dir={'': 'src'},
    project_urls={
        'Bug Reports': 'https://github.com/suetAndTie/CreditCardComparison/issues',
        'Source': 'https://github.com/suetAndTie/CreditCardComparison',
    },
)
