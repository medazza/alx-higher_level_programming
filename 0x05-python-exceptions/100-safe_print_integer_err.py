#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    is_intgr = True
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        is_intgr = False
    return (is_intgr)
