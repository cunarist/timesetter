cmake_minimum_required(VERSION 3.0.0)
project(set_system_time)

add_library(set_windows_time SHARED "./module/setsystemtime/on_windows.cpp")