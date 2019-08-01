from setuptools import setup

REQUIREMENTS = [
    'requests>=2.5',
    'six==1.12',
    'web3==4.9.2',
    'pytest>=4.4.0,<5.0.0',
    'tox==3.13.2',
    'setuptools',
    'eth_keys'
]

setup(
    name='dydx-python',
    version='0.1.0',
    packages=['dydx'],
    description='dYdX Python REST API for Limit Orders',
    url='https://github.com/dydxprotocol/dydx-python',
    author='dYdX Trading Inc.',
    license='Apache 2.0',
    author_email='contact@dydx.exchange',
    install_requires=REQUIREMENTS,
    keywords='dydx exchange rest api defi ethereum eth',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache License 2.0',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
