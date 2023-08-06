# pycrobit

[![Coverage Status](https://coveralls.io/repos/github/mixteen/pycrobit/badge.svg?branch=main)](https://coveralls.io/github/mixteen/pycrobit?branch=main)
[![PyPI version](https://badge.fury.io/py/pycrobit.svg)](https://badge.fury.io/py/pycrobit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

Python library that permits to recycle microbits exercises in python using 5 * 5
strings and some coloring without the hassle of handling terminal coloring and refresh.

## Context

There's a lot of fun exercises for children using microbits but a lot less using python.

## Installation

```bash
pip install pycrobit[colorama]
```

Or download ``pycrobit.py`` for offline use.

## Example of use

```python
from pycrobit import Fore, Pycrobit

all_lit = """
*****
*****
*****
*****
*****
"""
all_off = """
.....
.....
.....
.....
....."""


pycrobit = Pycrobit(framerate=0.50)
while True:
    pycrobit.display(all_lit)  # Lit red by default
    pycrobit.display(all_off)
    pycrobit.display(all_lit, {"*": Fore.YELLOW})
    pycrobit.display(all_off)
    pycrobit.display(all_lit, {"*": Fore.GREEN})
    pycrobit.display(all_off)
    pycrobit.display("*.*.*\n" * 5)
    pycrobit.wait(-0.25)
    pycrobit.display(".***." * 5)
    pycrobit.wait(-0.25)
```
