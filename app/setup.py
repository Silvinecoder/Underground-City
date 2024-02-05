from setuptools import setup, find_packages

setup(
    name='celiac-python',
    version='0.1.0',
    description='Celiac app',
    author='CSS',
    url='https://github.com/',
    packages=find_packages(exclude=['tests*']),
    install_requires=[
      'beautifulsoup4',
      'requests==2.28.2',
      'SQLAlchemy~=2.0.0'
    ],
)
