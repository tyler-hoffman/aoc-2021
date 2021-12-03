# advent of code 2021

[![tyler-hoffman](https://circleci.com/gh/tyler-hoffman/aoc-2021.svg?style=svg)](https://circleci.com/gh/tyler-hoffman/aoc-2021)

Python 3.10 edition

## Notes on the repo
* Package management is done with [Poetry](https://python-poetry.org/)
* utils in the `utils/` directory can/should be used to bootstrap new directories/files for solutions
* utils in the `utils/` derectory require [advent-of-code-data](https://github.com/wimglenn/advent-of-code-data), which relies on my session cookie. So don't use those unless you are me.

## Getting started
1. Make sure you have [Poetry](https://python-poetry.org/) installed
1. `poetry install`
1. If you are using utils that use `advent-of-code-data`, have my adventofcode session cookie stored in `~/.config/aocd/token` (note that this may be tricky if you are not me)

## Commands to run
| Purpose                         | Command |
|---------------------------------|---------|
| Run all tests                   | `poetry run python -m unittest` |
| Run specific test file          | `poetry run python -m unittest <FILE>` |
| Run solution file               | `poetry run python -m src.day_<DAY>.<PART>` (where `DAY` has a leading zero if needed) |
| Format code                     | `poetry run python -m black . --target-version py310` |
| Bootstrap files for new problem | `poetry run python -m utils.create_files -d <DAY> -p <PART>` |
| Submit solution                 | `poetry run python -m utils.submit -d <DAY> -p <PART>` |

## Handy links
* [AoC](https://adventofcode.com/2021)
* [Repo](https://github.com/tyler-hoffman/aoc-2021)
* [CI](https://app.circleci.com/pipelines/github/tyler-hoffman/aoc-2021)