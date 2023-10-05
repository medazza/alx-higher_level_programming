#!/usr/bin/python3

if __name__ == "__main__":
    """Print the add of all the arguments passed to it."""
    import sys

    sum_args = 0
    for i in range(len(sys.argv) - 1):
        sum_args += int(sys.argv[i + 1])
    print("{}".format(sum_args))
