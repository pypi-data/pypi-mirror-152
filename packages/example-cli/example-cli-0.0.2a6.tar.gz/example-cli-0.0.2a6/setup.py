# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['example_cli']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0']

entry_points = \
{'console_scripts': ['example-cli = example_cli.__main__:main']}

setup_kwargs = {
    'name': 'example-cli',
    'version': '0.0.2a6',
    'description': '',
    'long_description': None,
    'author': 'RincewindWizzard',
    'author_email': 'git@magierdinge.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
