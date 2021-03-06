# About
A Python package to set system time regardless of operating system
## Supported platforms
 - Windows
 - Linux
 - macOS
## Tips
 - This package aims to set system time in the precision of below milliseconds.
 - You need to pass a datetime object to the `set` function. If the timezone information was not included in the time object(naive), the package will assume that it's identical to the system.
 - You need to run your Python code with administration privileges for this package to work properly. Otherwise, `PermissionError` will be raised. This applies to all platforms.
## How to use
Install the package from PyPI
```
pip install timesetter
```
Then import it in your Python code
```
from datetime import datetime
import timesetter

target_time = datetime(year=2021, month=3, day=29, hour=15, minute=38, second=12)
timesetter.set(target_time)
```
