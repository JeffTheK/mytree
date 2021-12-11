from setuptools import setup

setup(
    name = "mytree",
    version = "0.1.0",
    description = "Lists directories",
    author = "JeffTheK",
    url = "https://github.com/JeffTheK/mytree",
    packages = ["mytree"],
    entry_points = {
        'console_scripts': [
            'mytree = mytree.__main__:main'
        ]
    },
)