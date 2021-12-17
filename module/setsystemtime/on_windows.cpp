#include <windows.h>
#ifdef _MSC_VER
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

extern "C" {
EXPORT void set_windows_time(int new_year, int new_month, int new_day,
                             int new_hour, int new_minute, int new_second,
                             int new_millisecond) {
  SYSTEMTIME new_time;

  new_time.wYear = new_year;
  new_time.wMonth = new_month;
  new_time.wDay = new_day;
  new_time.wHour = new_hour;
  new_time.wMinute = new_minute;
  new_time.wSecond = new_second;
  new_time.wMilliseconds = new_millisecond;

  SetSystemTime(&new_time);
}
}