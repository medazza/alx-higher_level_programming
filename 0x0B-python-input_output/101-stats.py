#!/usr/bin/python3
"""Module contain print_dict_sorted_nonzero"""


def print_dict_sorted_nonzero(status_codes):
    """Print status codes with nonzero value in numericalorder.

    Args:
        status_codes (dict): dictionary of status codes.
    """

    sorted_keys = sorted(status_codes.keys())
    print('\n'.join(["{:d}: {:d}".format(k, status_codes[k])
                     for k in sorted_keys if status_codes[k] != 0]))

if __name__ == "__main__":
    from sys import stdin

    try:
        total_size = 0
        status_codes = \
            {code: 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
        for n, lne in enumerate(stdin, 1):
            words = lne.split()
            total_size += int(words[-1])
            status_codes[int(words[-2])] += 1
            if n % 10 == 0:
                print("File size: {:d}".format(total_size))
                print_dict_sorted_nonzero(status_codes)
    finally:
        print("File size: {:d}".format(total_size))
        print_dict_sorted_nonzero(status_codes)
