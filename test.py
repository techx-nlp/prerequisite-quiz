# THIS FILE IS FOR TESTING YOUR CODE; DO NOT EDIT ITS CONTENT

import sys

import basics
import autograd
import interpreter


def log_func(code):
    return lambda x: print(f'\033[{code}m{x}\033[0m')


good = log_func(32)
bad = log_func(91)
bold = log_func(1)


def basics_test():
    pass