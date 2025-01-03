# User Guide

Timesetter is a Python package to set system time regardless of operating system

## Supported Platforms

- Windows
- Linux
- macOS

## Tips

- This package aims to set system time in the precision of below milliseconds.
- You need to pass a datetime object to the `set` function. If the timezone information was not included in the time object(naive), the package will assume that it's identical to the system.
- You need to run your Python code with administration privileges for this package to work properly. Otherwise, `PermissionError` will be raised. This applies to all platforms.

## How to Use

Install the package from PyPI

```shell
pip install timesetter
```

Then import it in your Python code

```python
from datetime import datetime
import timesetter

target_time = datetime(year=2021, month=3, day=29, hour=15, minute=38, second=12)
timesetter.set(target_time)
```

# For Maintainers

## Preparation

- The modern Python package manager [`uv`](https://docs.astral.sh/uv/) is used for dependency resolution. Please ensure it is installed on your system before proceeding.
- Code checking should always be enabled to maintain code quality. Make sure [Ruff](https://docs.astral.sh/ruff/) and [Pyright](https://microsoft.github.io/pyright/#/) are activated in your IDE.

## Command Line Scripts

Generate the distribution archive to `/dist`

```
uv build
```

Upload the package to PYPI

```
uv publish
```
