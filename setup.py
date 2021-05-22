import os

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="secure-fs",
    version="0.1.0",
    author="Freedom of the Press Foundation",
    author_email="securedrop@freedom.press",
    description="Library that ensures restrictive file permissions and safe paths when creating and working with files and directories.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GPLv3+",
    install_requires=[],
    python_requires=">=3.5",
    url="https://github.com/freedomofpress/secure-fs",
    packages=setuptools.find_packages(exclude=["tests"]),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
    ),
)
