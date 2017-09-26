import os
from setuptools import setup


with open(os.path.join(os.path.dirname(__file__), "VERSION"), "r") as f:
    VERSION_FILE = f.read().strip()
VERSION = VERSION_FILE.read().strip()

setup(
    name='hyperdash',
    packages=['hyperdash', 'hyperdash_cli'],
    install_requires=[
        'requests',
        'six>=1.10.0',
        'python-slugify',
    ],
    entry_points={
        'console_scripts': ['hyperdash = hyperdash_cli.cli:main']
    },
    version=VERSION,
    description='Hyperdash.io CLI and SDK',
    author='Hyperdash',
    author_email='support@hyperdash.io',
    url='https://hyperdash.io',
)
