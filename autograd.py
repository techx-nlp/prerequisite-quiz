# TechX NLP Coding Quiz: Autograd
#
# This file corresponds to Question 4.
#
# Please fill in the content of the following functions/classes
# according to the instructions given by the accompanying PDF file.
#
# Note that the template code in this problem merely serves as a
# guide; feel free to change it.


class Variable:

    def __init__(self, name):
        pass

    def evaluate(self, inputs):
        return

    def grad(self, respect_to, inputs):
        return

    def __add__(self, other):
        return self

    def __mul__(self, other):
        return self

    def __pow__(self, other):
        return self


class Constant:

    def __init__(self, value):
        pass

    def evaluate(self, inputs):
        return

    def grad(self, respect_to, inputs):
        return

    def __add__(self, other):
        return self

    def __mul__(self, other):
        return self

    def __pow__(self, other):
        return self