#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for ind in range(1, 3):
        try:
            if ind > a:
                raise Exception('Too far')
            result += a ** b / ind

        except Exception:
            result = b + a
            break
    return (result)
