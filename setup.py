import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='intersis_implementation',
    version='0.7.0',
    packages=['intersis_implementation'],
    include_package_data=True,
    description='An implementation of InterSIS/api.',
    long_description=README,
    url='https://intersis.org/',
    author='The Intersis Foundation',
    author_email='dev@intersis.org',
    install_requires=[
        'django>=1.8.7, <1.9',
        'djangorestframework>=3.3.2, <3.4',
        'django-rest-encrypted-lookup==0.10.1',
        'django-rest-serializer-field-permissions==1.0.0',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
