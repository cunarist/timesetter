import os
import platform
import ctypes
import time
from datetime import datetime


def to(time_object):

    # UTC 시각 기준으로 세팅

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
            int(time_object.microsecond / 1000),  # 밀리초
        )

    elif platform.system() == "Linux":

        time_tuple = (
            time_object.year,
            time_object.month,
            time_object.day,
            time_object.hour,
            time_object.minute,
            time_object.second,
            int(time_object.microsecond / 1000),  # 밀리초
        )
        clock_realtime = 0

        class TimeSpec(ctypes.Structure):
            _fields_ = [("tv_sec", ctypes.c_long), ("tv_nsec", ctypes.c_long)]

        librt = ctypes.CDLL(ctypes.util.find_library("rt"))

        ts = TimeSpec()
        ts.tv_sec = int(time.mktime(datetime(*time_tuple[:6]).timetuple()))
        ts.tv_nsec = time_tuple[6] * 1000000  # Millisecond to nanosecond

        # http://linux.die.net/man/3/clock_settime
        librt.clock_settime(clock_realtime, ctypes.byref(ts))

    elif platform.system() == "Darwin":  # macOS

        pass
