import os
import platform
import ctypes
import time
from datetime import datetime, timezone, timedelta


def set(time_object):

    # ■■■■■ check the datetime object ■■■■■

    if type(time_object) != datetime:
        raise TypeError("Argument needs to be a datetime object")

    if time_object.tzinfo is None:
        # if the object is timezone naive
        # apply the system timezone to the object
        system_timezone = timezone(timedelta(seconds=-time.timezone))
        time_object = time_object.replace(tzinfo=system_timezone)

    # now the time is represented in pure UTC timezone
    time_object = time_object.astimezone(timezone.utc)

    # ■■■■■ check administration privileges ■■■■■

    if platform.system() == "Windows":
        # on windows
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        # on unix
        is_admin = os.getuid() == 0

    if not is_admin:
        raise PermissionError(
            "Administrator privileges are needed to set the system time. Make sure"
            " you've run your Python code with administrator privileges."
        )

    # ■■■■■ change the system time ■■■■■

    if platform.system() == "Windows":

        this_folder, _ = os.path.split(__file__)
        dll_filepath = os.path.join(this_folder, "on_windows.dll")
        loaded_dll = ctypes.windll.LoadLibrary(dll_filepath)

        time_setter = loaded_dll["set_windows_time"]
        time_setter.argtypes = (
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_int,
        )
        time_setter.restype = ctypes.c_int

        time_setter(
            time_object.year,
            time_object.month,
            time_object.day,
            time_object.hour,
            time_object.minute,
            time_object.second,
            int(time_object.microsecond / 1000),  # convert to milliseconds
        )

    elif platform.system() == "Linux" or platform.system() == "Darwin":
        # unix: linux or macOS
        # https://docs.python.org/ko/3.10/library/time.html#time.clock_settime

        # system-wide real-time clock
        realtime_clock_id = time.CLOCK_REALTIME

        timestamp = time_object.timestamp()
        time.clock_settime(realtime_clock_id, timestamp)
