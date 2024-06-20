# Quick Start

Ecosystem Plugin for Scroll support in Ape.

## Dependencies

- [python3](https://www.python.org/downloads) version 3.9 or greater, python3-dev

## Installation

### via `ape`

You can install this plugin using `ape`:

```bash
ape plugins install scroll
```

or via config file:

```yaml
# ape-config.yaml
plugins:
  - name: scroll
```

### via `pip`

You can install the latest release via [`pip`](https://pypi.org/project/pip/):

```bash
pip install ape-scroll
```

### via `setuptools`

You can clone the repository and use [`setuptools`](https://github.com/pypa/setuptools) for the most up-to-date version:

```bash
git clone https://github.com/theref/ape-scroll.git
cd ape-scroll
python3 setup.py install
```

## Quick Usage

Installing this plugin adds support for the Scroll ecosystem:

```bash
// sepolia testnet
ape console --network scroll:testnet

// mainnet
ape console --network scroll:mainnet
```

For some potential rpc endpoints, see https://chainlist.org/?search=scroll&testnets=true

## Development

This project is in development and should be considered a beta.
Things might not be in their final state and breaking changes may occur.
Comments, questions, criticisms and pull requests are welcomed.
