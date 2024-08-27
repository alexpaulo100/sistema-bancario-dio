from setuptools import setup, find_packages


setup(
    name="bcdio",
    version="0.1.0",
    description="Sistema Bancario",
    author="Alex Silva",
    packages=["bcdio"],
    entry_points={
        "console_scripts": ["bcdio = bcdio.__main__:main"
        ]
    },
    

)