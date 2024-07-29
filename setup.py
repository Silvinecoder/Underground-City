from setuptools import setup, find_packages

setup(
    name='underground-city',
    version='0.1.0',
    description='Celiac app backend',
    author='CSS',
    url='https://github.com/Silvinecoder/san',
    packages=find_packages(),
    install_requires=[
      'beautifulsoup4',
      'requests==2.28.2',
      'SQLAlchemy~=2.0.0'
    ],
)
