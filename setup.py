from setuptools import setup, find_packages

setup(
    name='cassandra-csv',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Export cassandra query result to CSV',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
    ],
    install_requires=[],
    url='https://github.com/wmarquardt/cassandra-csv',
    author='William Marquardt',
    author_email='williammqt@gmail.com'
)
