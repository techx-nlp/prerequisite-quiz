# THIS FILE IS FOR TESTING YOUR CODE; DO NOT EDIT ITS CONTENT

import os
import sys

import basics
import autograd
import interpreter


def supports_color():
    supported = sys.platform != 'Pocket PC' and \
        (sys.platform != 'win32' or 'ANSICON' in os.environ)

    is_a_tty = hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
    return supported and is_a_tty


def log_func(code):
    return (lambda x: print(f'\033[{code}m{x}\033[0m')) \
        if supports_color() else print


good = log_func('32')
bad = log_func('91')
bold = log_func('1')
failure = log_func('1;91')


def abort():
    print()
    failure('TEST FAILED')
    sys.exit(1)


def assert_equal(output, expected):
    if output == expected:
        good(f'Test Passed: {output}')
    else:
        bad(f'Test Failed: Expected {expected}, instead got {output}')
        abort()


def test(module, test_set):
    bold(f'Testing File "{module.__name__}.py":')
    print()

    for func_name in test_set:
        bold(f'Testing Function "{func_name}"')
        func = getattr(module, func_name, None)

        if func is None:
            bad(
                f'Function "{func_name}" not found in file '
                f'"{module.__name__}.py"'
            )
            abort()

        for args, answer in test_set[func_name]:
            assert_equal(func(*args), answer)

        print()


# ((*inputs), expected)
basics_set = {
    'greatest_common_factor': [
        ((10, 5), 5),
        ((63, 84), 21),
        ((969, 171), 57),
        ((261, 2001), 87),
        ((2669, 2983), 157)
    ],
    'reorder': [
        (
            ([3, 2, 2, 1, 3], 2),
            [3, 1, 3, 2, 2]
        ),
        (
            ([25, 25, 22, 24, 23, 23, 23, 23, 22, 20], 7),
            [25, 25, 22, 24, 23, 23, 23, 23, 22, 20]
        ),
        (
            ([97, 95, 99, 91, 93, 100, 96, 91, 100, 92, 96, 92, 91], 100),
            [97, 95, 99, 91, 93, 96, 91, 92, 96, 92, 91, 100, 100]
        ),
        (
            ([-2, -3, -5, 1, 4, 5, -3, 0, -1, 3, 2, 5, -2, 4, -3], -2),
            [-3, -5, 1, 4, 5, -3, 0, -1, 3, 2, 5, 4, -3, -2, -2]
        ),
        (
            ([-2, -1, 2, 2, 2, 0, -2, 0, -2, -1, 2, 1, -1, -2, -2], 0),
            [-2, -1, 2, 2, 2, -2, -2, -1, 2, 1, -1, -2, -2, 0, 0]
        )
    ]
}


test(basics, basics_set)
good('ALL TEST PASSED')