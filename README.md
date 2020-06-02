# Venom

[![Build Status](https://travis-ci.org/best-doctor/we_are_venom.svg?branch=master)](https://travis-ci.org/best-doctor/we_are_venom)
[![Maintainability](https://api.codeclimate.com/v1/badges/18b141ed6576e8b6405a/maintainability)](https://codeclimate.com/github/best-doctor/we_are_venom/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/18b141ed6576e8b6405a/test_coverage)](https://codeclimate.com/github/best-doctor/we_are_venom/test_coverage)

Checks which modules developer contributed using git history.

DISCLAIMER: I use DDD, it might not work or work not as described here. Stay calm.

## Installation

```terminal
pip install we-are-venom
```

## Usage

First, provide module structure configuration in `setup.cfg`, `venom` section:

```terminal
[venom]
history_depth_years=2
min_lines_in_file=20
extensions_to_check=py,html,css,md,cfg,js,ts
min_new_lines_for_accumulated_module=50
modules=
    apps/foo
    apps/bar
    scripts
    core
```

Check total accumulation level:

```terminal
venom check --verbose melevir@gmail.com .

---------------------------------------------------------
|   Module  | Total lines | Touched lines | Accumulated |
---------------------------------------------------------
| apps/foo  | 120         | 106           | ✅          |
| apps/bar  | 6           | 0             | -           |
| scripts   | 620         | 14            | ❌          |
| core      | 1865        | 215           | ✅          |
---------------------------------------------------------
Total accumulation rate: 66%
```
