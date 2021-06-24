from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='listofobj',
    version='0.0.1',
    description='List of Object custom implementation',
    long_description=long_description,
    license='GNU GENERAL PUBLIC LICENSE',
    packages=['listofobj'], #     install_requires=['json', 'urllib'],
    author='Daniele Beninato',
    author_email='db.stuff+github@outlook.it',
    keywords=['listofobj'],
    url='https://github.com/dabenny/ListOfObjects'
)