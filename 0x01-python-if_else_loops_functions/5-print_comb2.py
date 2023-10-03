#!/usr/bin/python3
for n in range(100):
    if n == 99:
        print(f"{n:d}")
    else:
        print(f"{n:02}", end=", ")

