import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="flaskreactapp",
    version="v1.0.10".replace('v',''),
    author="Ilya Shnayderman",
    author_email="ilyashn@il.ibm.com",
    description="Flask and react application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ilyashnil/flash-react-app",
    packages=setuptools.find_packages(),
    license='Apache License 2.0',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)