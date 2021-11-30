# advent of code 2021

Python edition

## Getting started
1. `python3 -m venv venv`
1. `source venv/bin/activate`
1. `python3 -m pip install --requirement requirements.txt`

## Commands to run
| Purpose                         | Command |
|---------------------------------|---------|
| Use virtual env                 | `python3 -m venv venv` |
| Deactivate virtual env          | `deactivate` |
| Run all tests                   | `python -m unittest` |
| Run specific test file          | `python -m unittest <FILE>` |
| Run solution file               | `src.day_<DAY>.<PART>` |
| Bootstrap files for new problem | `python -m utils.boilerplate.boilerplate -d <DAY> -p <PART>` |
| Format code                     | `python -m black .` |
