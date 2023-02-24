from setuptools import setup, find_packages
from codecs import open
from os import path

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="quick_styles",
    version="1.0.0",
    description="A ridiculously lightweight Python library for effortlessly applying ANSI escape color & style codes to Windows CMD.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/imjamnotjelly/quick_styles",
    author="imjamnotjelly",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=find_packages(include=['quick_styles']),
)