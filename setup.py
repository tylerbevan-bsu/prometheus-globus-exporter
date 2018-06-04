from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='server_report',
    version='0.1.0a1',
    description='Prometheus globus exporter',
    long_description=long_description,
    url='https://github.com/tylerbevan-bsu/prometheus-globus-exporter',
    author='Tyler Bevan',
    author_email='tylerbevan@boisestate.edu',
    license='BSD 3-clause License',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='prometheus globus reporting',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['globus_sdk', 'prometheus_client'],
    entry_points={
        'console_scripts': [
            'prometheus-globus-exporter=exporter.main:main',
        ],
    },
)
