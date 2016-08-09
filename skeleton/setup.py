try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Cuap',
    'url': 'www.cuap-cuap.dev',
    'download_url': 'www.cuap-cuap.dev',
    'author_email': 'cuapcuap@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'cuapcuap'
}

setup(**config)
