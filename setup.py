from platform import python_version
from sys import exit, version_info
from setuptools import setup, find_packages

if version_info < (3,):
    print('Error: Python 3 required but found %s' % python_version())
    exit(1)

with open('requirements.txt', 'r') as infile:
    install_requires = infile.read().split('\n')

with open('README.rst', 'r') as infile:
    long_description = infile.read()

with open('owncloud_news_updater/version.txt', 'r') as infile:
    version = ''.join(infile.read().split())

setup(
    name='owncloud_news_updater',
    version=version,
    description='ownCloud News updater - Fast updates for your RSS/Atom feeds',
    long_description=long_description,
    author='Bernhard Posselt',
    author_email='dev@bernhard-posselt.com',
    url='https://github.com/owncloud/news',
    packages=find_packages(),
    include_package_data=True,
    license='GPL',
    install_requires=install_requires,
    keywords=['owncloud', 'news', 'updater'],
    classifiers=[
        'Intended Audience :: System Administrators',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 or later ('
        'GPLv3+)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Utilities'
    ],
    entry_points={
        'console_scripts': [
            'owncloud-news-updater = owncloud_news_updater.application:main'
        ]
    }
)