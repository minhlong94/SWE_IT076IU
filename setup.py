import sys

import setuptools

try:
    from pipenv.project import Project
    from pipenv.utils import convert_deps_to_pip

    pipfile = Project(chdir=False).parsed_pipfile

    packages = pipfile["packages"].copy()
    requirements = convert_deps_to_pip(packages, r=False)
except ImportError:
    requirements = [
        "streamlit>=0.70.0",
        "pandas>=1.1.3",
        "bcrypt>=3.2.0",
        "plotly>=4.13.0",
        "hiplot>=0.1.20",
        "pandas-profiling>=2.9.0",
        "click>=7.1.2",
        "numpy==1.19.3"
    ]
except Exception as e:
    sys.exit(e)

__version__ = "0.1.0dev0"
__name__ = "WMS"
__description__ = "A wholesale management system application created with Streamlit."


def readme():
    """print long description"""
    with open('README.md') as f:
        return f.read()


setuptools.setup(
    name=__name__,
    version=__version__,
    description=__description__,
    long_description=readme(),
    url="https://github.com/Doki064/SWE_IT076IU/tree/dev",
    license="MIT",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    project_urls={
        "Source": "https://github.com/Doki064/SWE_IT076IU/tree/dev",
        "Origin": "https://github.com/minhlong94/SWE_IT076IU",
    },
    packages=setuptools.find_packages(),
    # Requirements
    install_requires=requirements,
    python_requires=">=3.7, <3.9",
    include_package_data=True,  # copy html and friends
    entry_points={"console_scripts": ["wms = wms.cli:main"]},
    scripts=["bin/wms.cmd"],
)
