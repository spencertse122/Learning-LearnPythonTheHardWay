try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'This is a game reflecting the throat cutting office scene',
    'author': 'Spencer Tse',
    'url': 'http://officesurvivor.com/project/',
    'download_url': 'http://officesurvivor.com/download/',
    'author_email': 'spencertse122@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['office_survivor'],
    'scripts': [],
    'name': 'office_survivor'
}

setup(**config)
