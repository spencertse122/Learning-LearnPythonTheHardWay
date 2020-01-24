try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'This is a test project, I have no idead what is going to happen',
    'author': 'Spencer Tse',
    'url': 'www.google.com',
    'download_url': 'www.youtube.com',
    'author_email': 'spencertse122@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
