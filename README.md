# Git Conflict Calculator

A small Python command-line calculator built for the UCS 745 Cloud and DevOps lab
by HARSH BADHAN (102317140, 4Q16). The code is deliberately simple: the point of the
repository is its Git history, which shows branching, merging and the manual
resolution of a merge conflict.

## Usage

```bash
python calculator.py 8 / 2      # prints 4.0
python calculator.py 5 + 7      # prints 12.0
```

## Running the tests

```bash
python -m unittest -v
```

## Branches

| Branch | Purpose |
| --- | --- |
| `main` | Stable code |
| `feature/friendly-error` | Returns a readable message when dividing by zero |
| `feature/strict-error` | Raises an exception when dividing by zero |
