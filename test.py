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
    global exit_code
    exit_code = 1


def assert_equal(output, expected, meta=''):
    if output == expected:
        good(f'Test Passed{meta}: {output}')
    else:
        bad(f'Test Failed{meta}: Expected {expected}, instead got {output}')
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
        else:
            for args, answer in test_set[func_name]:
                assert_equal(func(*args), answer)

        print()


def autograd_test():
    bold(f'Testing File "autograd.py":')
    print()

    Variable = getattr(autograd, 'Variable', None)
    C = getattr(autograd, 'Constant', None)

    if Variable is None:
        bad('Class "Variable" not found in file "autograd.py"')
        abort()

    if C is None:
        bad('Class "Constant" not found in file "autograd.py"')
        abort()

    if Variable is None or C is None:
        print()
        return

    bold(f'Testing Equation (3 * x + 2) ^ 3 * (5 * y + 7 * x) ^ 2')
    x = Variable(name='x')
    y = Variable(name='y')
    equation = (C(3) * x + C(2)) ** C(3) * (C(5) * y + C(7) * x) ** C(2)

    assert_equal(
        equation.grad('x', {'x': 10, 'y': 2}),
        95682560,
        ' (dx; x: 10, y: 2)'
    )

    assert_equal(
        equation.grad('y', {'x': 5, 'y': 3}),
        2456500,
        ' (dy; x: 5, y: 3)'
    )

    assert_equal(
        equation.grad('y', {'x': 0.5, 'y': 1.5}),
        4716.25,
        ' (dy; x: 0.5, y: 1.5)'
    )

    print()
    bold(f'Testing Equation 3 * (x + y + z) ^ 2 + 2 * y * x * z')
    x = Variable(name='x')
    y = Variable(name='y')
    z = Variable(name='z')
    equation = C(3) * (x + y + z) ** C(2) + C(2) * y * x * z

    assert_equal(
        equation.grad('x', {'x': 7, 'y': 2, 'z': 3}),
        84,
        ' (dx; x: 7, y: 2, z: 3)'
    )

    assert_equal(
        equation.grad('y', {'x': 2, 'y': 3, 'z': 1.5}),
        45.0,
        ' (dy; x: 2, y: 3, z: 1.5)'
    )

    assert_equal(
        equation.grad('z', {'x': 1.5, 'y': 2, 'z': 0.25}),
        28.5,
        ' (dz; x: 1.5, y: 2, z: 0.25)'
    )

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
    ],
    'special_sum': [
        (([16, 19, 2, 6, 12, 20, 14, 7, 9, 20],), 55),
        (([6, 7, 7, 6, 7, 4, 6, 6, 2, 2, 5, 2, 6, 2, 6],), 22),
        (([26, 46, 39, 5, 50, 15, 47, 32, 36, 38, 1, 9, 10, 40, 29],), 133),
        (([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],), -225),
        (([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],), -105)
    ]
}

interpreter_set = {
    'interpreter': [
        (
            ('a = 5\nb = 10\nc = add a b\nnoutput c\noutput b',),
            [15, 10]
        ),
        (
            ('  my_var   =29\nout= 1\nc =  add my_var out\nnoutput    c',),
            [30]
        ),
        (
            ('output   15\nfoo = div 35 7\noutput foo',),
            [15, 5]
        ),
        (
            ('a = 2\noutput a\na = mul a a\noutput a\na = mul a a\noutput a',),
            [2, 4, 8]
        ),
        (
            ('var = 10\ntest=20  \nw=sub test var\noutput w\noutput w',),
            [10, 10]
        )
    ]
}


exit_code = 0

test(basics, basics_set)
autograd_test()
test(interpreter, interpreter_set)

if exit_code == 0:
    good('ALL TEST PASSED')
else:
    failure('TEST FAILED')
    sys.exit(1)