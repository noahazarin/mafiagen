try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Generate Newbie Mafia setups for TL Mafia',
    'author': 'Noah Azarin',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it',
    'author_email': 'noahazarin@gmail.com',
    'version': '0.1',
    'install_Requires': ['nose'],
    'packages': ['mafiagen'],
    'scripts': [],
    'name': 'mafiagen',
}

setup(**config)
