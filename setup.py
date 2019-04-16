from setuptools import setup, find_packages

setup(
    name='cassandra-csv',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Export cassandra query result to CSV',
    install_requires=[],
    url='https://github.com/wmarquardt/cassandra-csv',
    author='William Marquardt',
    author_email='williammqt@gmail.com'
)
