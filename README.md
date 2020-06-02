# Venom

[![Build Status](https://travis-ci.org/best-doctor/we_are_venom.svg?branch=master)](https://travis-ci.org/best-doctor/we_are_venom)
[![Maintainability](https://api.codeclimate.com/v1/badges/18b141ed6576e8b6405a/maintainability)](https://codeclimate.com/github/best-doctor/we_are_venom/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/18b141ed6576e8b6405a/test_coverage)](https://codeclimate.com/github/best-doctor/we_are_venom/test_coverage)

Checks which modules developer contributed using git history.

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

`modules` variable is required, others are optional.

Check total accumulation level:

```terminal
$ venom check melevir@gmail.com .
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┓
┃ Module                         ┃ Total lines ┃ Touched lines ┃ Accumulated ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━┩
│ opensource_watchman/pipelines/ │ 557         │ 120           │ ✅          │
│ opensource_watchman/utils/     │ 30          │ 30            │ ❌          │
│ opensource_watchman/templates/ │ 105         │ 127           │ ✅          │
│ opensource_watchman/api/       │ 218         │ 12            │ ❌          │
│ tests/                         │ 8           │ 16            │ -           │
│ opensource_watchman/api/       │ 218         │ 0             │ ❌          │
│ opensource_watchman/pipelines/ │ 557         │ 0             │ ❌          │
│ opensource_watchman/templates/ │ 105         │ 0             │ ❌          │
│ opensource_watchman/utils/     │ 30          │ 0             │ ❌          │
│ tests/                         │ 8           │ 0             │ -           │
└────────────────────────────────┴─────────────┴───────────────┴─────────────┘
Total accumulation rate: 25%
```
