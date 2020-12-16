import os
import sys

import setuptools
from setuptools.command.install import install

VERSION = "0.1.1dev0"
NAME = "WMS"
DESCRIPTION = "A wholesale management system application created with Streamlit."


def readme():
    """print long description"""
    with open('README.md') as f:
        return f.read()


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""

    description = "verify that the git tag matches our version"

    def run(self):
        tag = os.getenv("CIRCLE_TAG")

        if tag != VERSION:
            info = "Git tag: {0} does not match the version of this app: {1}".format(
                tag, VERSION
            )
            sys.exit(info)


setuptools.setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=readme(),
    url="https://github.com/Doki064/SWE_IT076IU",
    license="MIT",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    project_urls={
        "Source": "https://github.com/Doki064/SWE_IT076IU",
        "Origin": "https://github.com/minhlong94/SWE_IT076IU",
    },
    packages=setuptools.find_packages(),
    # Requirements
    install_requires=[
        "streamlit>=0.72.0",
        "pandas>=1.1.3",
        "bcrypt>=3.2.0",
        "plotly>=4.13.0",
        "hiplot>=0.1.20",
        "pandas-profiling>=2.9.0",
        "click>=7.1.2",
        "numpy==1.19.3",
    ],
    python_requires=">=3.7, <3.9",
    include_package_data=True,
    entry_points={"console_scripts": ["wms = wms.cli:main"]},
    scripts=["bin/wms.cmd"],
    cmdclass={
        "verify": VerifyVersionCommand,
    },
)
