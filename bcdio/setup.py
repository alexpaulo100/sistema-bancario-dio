from setuptools import setup, find_packages

setup(
    name="bcdio",
    version="0.1.1",
    description="Sistema Bancario",
    author="Alex Silva",
    packages=find_packages(),
    install_requires=[
        "sqlmodel>=0.0.22",
        "validate-docbr>=1.10.0",
        "click>=8.1.8",
    ],
    entry_points={"console_scripts": ["bcdio = bcdio.__main__:main"]},
)
