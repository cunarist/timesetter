cmake_minimum_required(VERSION 3.0.0)
project(timesetter)

add_library(set_windows_time SHARED "./module/timesetter/on_windows.cpp")