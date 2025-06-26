cmake_minimum_required(VERSION 3.13)
project(HandsOnInternetSecurity)

set(CMAKE_CXX_STANDARD 14)

add_executable(Redirection reverse-shell/redirection.c)