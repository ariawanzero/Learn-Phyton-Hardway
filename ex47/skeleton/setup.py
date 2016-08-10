try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Project Test',
    'author': 'Ariawan',
    'url': 'www.cupau.com',
    'download_url': 'www.cupau.com',
    'author_email': 'ariawan.zero@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'learn-python'
}

setup(**config)
