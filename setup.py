from setuptools import find_packages, setup


with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as req:
    requirements = req.readlines()


setup(
    name="rvtools_python",
    version="1.0.0",
    author="Waldirio",
    author_email="waldirio@gmail.com",
    description="Simple app to collect information from vSphere",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    url="https://github.com/waldirio/rvtools_python/",
    packages=find_packages(),
    python_requires=">=3.9",
    scripts=['bin/rvtools'],
    include_package_data=True,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
