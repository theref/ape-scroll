#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

extras_require = {
    "test": [  # `test` GitHub Action jobs uses this
        "pytest>=6.0",  # Core testing package
        "pytest-mock",  # For patching and mocking
        "pytest-xdist",  # multi-process runner
        "pytest-cov",  # Coverage analyzer plugin
        "hypothesis>=6.2.0,<7.0",  # Strategy-based fuzzer
    ],
    "lint": [
        "black>=22.12.0",  # auto-formatter and linter
        "mypy>=0.991",  # Static type analyzer
        "flake8>=5.0.4",  # Style linter
        "isort>=5.10.1",  # Import sorting linter
        "types-setuptools",  # Needed due to mypy typeshed
        "mdformat>=0.7.16",  # Auto-formatter for markdown
        "mdformat-gfm>=0.3.5",  # Needed for formatting GitHub-flavored markdown
        "mdformat-frontmatter>=0.4.1",  # Needed for frontmatters-style headers in issue templates
    ],
    "doc": [
        "myst-parser>=0.17.0,<0.18",  # Tools for parsing markdown files in the docs
        "sphinx-click>=3.1.0,<4.0",  # For documenting CLI
        "Sphinx>=4.4.0,<5.0",  # Documentation generator
        "sphinx_rtd_theme>=1.0.0,<2",  # Readthedocs.org theme
        "sphinxcontrib-napoleon>=0.7",  # Allow Google-style documentation
    ],
    "release": [  # `release` GitHub Action job uses this
        "setuptools",  # Installation tool
        "setuptools-scm",  # Installation tool
        "wheel",  # Packaging tool
        "twine",  # Package upload tool
    ],
    "dev": [
        "commitizen",  # Manage commits and publishing releases
        "pre-commit",  # Ensure that linters are run prior to committing
        "pytest-watch",  # `ptw` test watcher/runner
        "ipdb",  # Debugger (Must use `export PYTHONBREAKPOINT=ipdb.set_trace`)
    ],
}

# NOTE: `pip install -e .[dev]` to install package
extras_require["dev"] = (
    extras_require["test"]
    + extras_require["lint"]
    + extras_require["doc"]
    + extras_require["release"]
    + extras_require["dev"]
    # NOTE: Do *not* install `recommended-plugins` w/ dev
)

with open("./README.md") as readme:
    long_description = readme.read()


setup(
    name="ape-scroll",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    description="""ape-scroll: Ape Ecosystem Plugin for Scroll""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="James Campbell",
    author_email="james.campbell@tanti.org.uk",
    url="https://github.com/theref/ape-scroll",
    include_package_data=True,
    install_requires=[
        "eth-ape>=0.8.1,<0.9",
    ],
    python_requires=">=3.9,<4",
    extras_require=extras_require,
    py_modules=["ape_scroll"],
    license="Apache-2.0",
    zip_safe=False,
    keywords="ethereum",
    packages=find_packages(exclude=["tests", "tests.*"]),
    package_data={"ape_scroll": ["py.typed"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
