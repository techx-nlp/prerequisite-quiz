# THIS FILE IS FOR TESTING YOUR CODE; DO NOT EDIT ITS CONTENT

import sys

import basics
import autograd
import interpreter


def log_func(code):
    return lambda x: print(f'\033[{code}m{x}\033[0m')


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
        ((63, 84), 7),
        ((2669, 2983), 157)
    ]
}


test(basics, basics_set)
good('ALL TEST PASSED')