# Venom

[![Build Status](https://travis-ci.org/best-doctor/we_are_venom.svg?branch=master)](https://travis-ci.org/best-doctor/we_are_venom)
[![Maintainability](https://api.codeclimate.com/v1/badges/18b141ed6576e8b6405a/maintainability)](https://codeclimate.com/github/best-doctor/we_are_venom/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/18b141ed6576e8b6405a/test_coverage)](https://codeclimate.com/github/best-doctor/we_are_venom/test_coverage)
[![PyPI version](https://badge.fury.io/py/we_are_venom.svg)](https://badge.fury.io/py/we_are_venom)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/we_are_venom)](https://pypi.org/project/we_are_venom/)

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

Generate report for Grand Code Review:

```terminal
$ venom grand-code-review . 2020-05-01 2020-06-01 https://github.com/best-doctor/import_me/ --min_lines=100 --module=finance --module=chat --generate_pretty_changesets
# TODO
Ticket num
    Info:
        Touched lines: 23
        Touched modules: finance
        Authors: melevir
    Commits:
        commit1 (link)
        commit2 (link)
...
Summary: total tickets, total commits, total loc in report and filtered.
```

This one groups commits by ticket number, filters out commits groups, that
touched more that `min_lines` lines or touched files in `module` (can be
multiple). If `generate_pretty_changesets`, than every group is cherry
picked to separate branch to generate pretty diff view.

## Contributing

We would love you to contribute to our project. It's simple:

- Create an issue with bug you found or proposal you have.
  Wait for approve from maintainer.
- Create a pull request. Make sure all checks are green.
- Fix review comments if any.
- Be awesome.

Here are useful tips:

- You can run all checks and tests with `make check`. Please do it
  before TravisCI does.
- We use
  [BestDoctor python styleguide](https://github.com/best-doctor/guides/blob/master/guides/en/python_styleguide.md).
- We respect [Django CoC](https://www.djangoproject.com/conduct/).
  Make soft, not bullshit.
