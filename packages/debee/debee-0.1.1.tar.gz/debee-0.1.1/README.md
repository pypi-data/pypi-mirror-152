# debee
[![pytest](https://github.com/ffreemt/debee/actions/workflows/routine-tests.yml/badge.svg)](https://github.com/ffreemt/debee/actions)[![python](https://img.shields.io/static/v1?label=python+&message=3.8&color=blue)](https://www.python.org/downloads/)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/debee.svg)](https://badge.fury.io/py/debee)

align de-en texts, fast

## Pre-install

`pyicu`, `pycld2`, `fasttext` (`polyglot` depends on `pyicu` and `pycld2` while fastlid depends on `fasttext`).
### Linux and friends
For example for Ubuntu
```bash
apt-get install libicu-dev pkg-config
pip install pyicu==2.8 pycld2 fasttext
# poetry add pyicu==2.8 pycld2 fasttext
```
### Windows
```
# https://www.lfd.uci.edu/~gohlke/pythonlibs/, e.g.
pip install pycld2-0.41-cp38-cp38-win_amd64.whl PyICU-2.8.1-cp38-cp38-win_amd64.whl fasttext-0.9.2-cp38-cp38-win_amd64.whl
```
If you have C++ in your Windows, simply ``pip install pyicu==2.8 pycld2 fasttext`` as for Linux.

## Install it

```shell
pip install git+https://github.com/ffreemt/debee
# poetry add git+https://github.com/ffreemt/debee
# git clone https://github.com/ffreemt/debee && cd debee
```

## Use it
```python
from debee import debee

```
