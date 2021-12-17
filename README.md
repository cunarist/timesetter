# About
A Python package to set system time regardless of operating system
## Support status
 - Windows: Yes
 - Linux: Yes
 - macOS: No
## Tips
On Windows, you need to run your Python code with administration privileges for this package to work properly. Otherwise, `PermissionError` will be raised.
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
