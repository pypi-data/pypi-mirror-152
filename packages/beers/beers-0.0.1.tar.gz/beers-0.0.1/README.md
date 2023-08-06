# BeER

<p align="center">
    <a href="https://github.com/lucmos/nn-template"><img alt="NN Template" src="https://shields.io/badge/nn--template-0.0.2-emerald?style=flat&labelColor=gray"></a>
    <a href="https://www.python.org/downloads/"><img alt="Python" src="https://img.shields.io/badge/python-3.9-blue.svg"></a>
    <a href="https://black.readthedocs.io/en/stable/"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

Better Enabled Resources


## Installation

```bash
pip install git+ssh://git@github.com/grok-ai/beer.git
```


## Quickstart

[comment]: <> (> Fill me!)


## Development installation

Setup the development environment:

```bash
git clone git+ssh://git@github.com/grok-ai/beer.git
conda env create -f env.yaml
conda activate beer
pre-commit install
```

Run the tests:

```bash
pre-commit run --all-files
pytest -v
```


### Update the dependencies

Re-install the project in edit mode:

```bash
pip install -e .[dev]
```
