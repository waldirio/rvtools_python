import setuptools


def long_description():
    with open("README.md", "r") as fh:
        return fh.read()


setuptools.setup(
    name="rvtools_python",
    version="0.0.1",
    author="Waldirio",
    author_email="waldirio@gmail.com",
    description="Simple app to collect information from vSphere",
    long_description=long_description(),
    url="https://github.com/waldirio/rvtools_python/",
    packages=setuptools.find_packages(),
    scripts=['bin/rvtools'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
