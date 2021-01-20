try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description' : 'Exercise 48',
    'author' : 'Spencer Tse',
    'url' : 'URL to get it at.',
    'download_url' : 'Where to download it.',
    'author_email' : 'My email.',
    'version' : '0.1',
    'install_requires' : ['nose'],
    'packages' : ['NAME'],
    'scripts' : [],
    'name' : 'Ex.48'
}

setup(**config)
