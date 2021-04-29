try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description' : 'Exercise 47',
    'author' : 'Spencer Tse',
    'url' : 'www.google.com',
    'download_url' : 'Where to download it.',
    'author_email' : 'spencertse122@gmail.com.',
    'version' : '0.1',
    'install_requires' : ['nose', 'pytest'],
    'packages' : ['NAME'],
    'scripts' : [],
    'name' : 'Learn Python The Hard Way'
}

setup(**config)
