# Coding Quiz

**Estimated Completion Time:** 1 hour

This quiz assesses the student's ability to program and solve problems in Python.

## Instructions

- There are 3 Python files that you need to complete: `basics.py`, `autograd.py` and `interpreter.py`
- Do not import/use any libraries in your program
- You can use the `test.py` script to test your programs
- Do not edit `test.py`

## Basics

The `basics.py` section tests your familiarity with basic Python syntax and programming. It contains 3 sub-problems.

### Greatest Common Factor (`greatest_common_factor`)

Write a function `greatest_common_factor` that returns the greatest common factor of the two given integers:

```python
def greatest_common_factor(a, b):
    return
```

Sample output:

```python
greatest_common_factor(30, 20) # 10
greatest_common_factor(45, 30) # 15
greatest_common_factor(159, 265) # 53
```

### Reorder (`reorder`)

Write a function `reorder` that takes a list of numbers and a number, and moves all list elements that are equal to the given number to the end of the list (not in-place; return the moved list as a new list).

```python
def reorder(num_list, num):
    return
```

Sample output:

```python
reorder([3, 4, 7, 6, 9, 3, 5, 9, 3, 2], 3) # [4, 7, 6, 9, 5, 9, 2, 3, 3, 3]
reorder([-2, -1, 0, 3, -2, -1, 1], 0) # [-2, -1, 3, -2, -1, 1, 0]
reorder([1, 2, 3], 10) # [1, 2, 3]
```

### Special Sum (`special_sum`)

Write a function `special_sum` that takes a list of numbers (positive integers), and return the sum of all even numbers minus the sum of all odd numbers.

```python
def special_sum(num_list):
    return
```

Sample output:

```python
special_sum([1, 2, 3]) # -2
special_sum([3, 2, 6, 9, 0]) # -4
special_sum([1, 2, 3, 4, 5, 6, 7, 8]) # 4
```

## Autograd

The `autograd.py` section tests your understanding of mathematical concepts such as derivatives and chain rule. This section has only one problem: you need to implement a very simple "autograd" system.

"Autograd" automatically builds a differentiation graph (or calculation graph) as the program carries out arithemetic operations. Consider this python expression:

```python
y = (m * x) + b
```

Its computational graph might look like:
```
        y
        |
        +
       / \
      K   b
     /
    *
   / \
  m   x
```

With this in mind, create a `Variable` and `Constant` class such that they support evaluation and partial differentiation as illustrated below:
```python
>>> x = Variable(name='x')
>>> m = Variable(name='m')
>>> c = Constant(5)
>>>
>>> y = m * x * c
>>>
>>> y.evaluate(inputs={'m': 10, 'x': 15}) # calculate the value of y
750
>>>
>>> y.grad(respect_to='x', inputs={'m': 2, 'x': 5}) # calculate the derivative of y in respect to x
10
```

Chains should also be supported:
```python
>>> a = Variable(name='e')
>>> b = Variable(name='r')
>>> c = Constant(4)
>>> y = (a + b) ** c
>>>
>>> y.grad(respect_to='e', inputs={'e': 3, 'r': 2})
500
```

Here's another example:
```python
>>> x = Variable(name='x')
>>> a = Constant(3) * (x + Constant(5))
>>> b = Constant(8) * (x - Constant(20))
>>> c = a / b
>>>
>>> c.evaluate({'x': 30})
1.3125
>>>
>>> c.grad('x', {'x': 10})
-0.09375
```

The following operations should be supported:
- Addition(+)
- Subtraction(-)
- Multiplication(\*)
- Division(/)
- Power(\*\*)

## Notes

- The power term `c` will always be a constant in any `a ^ c` for simplicity
- If you are not familar with overriding the behavior of operators (`+`, `-`, `*`, etc) in Python, check out [this tutorial](https://www.geeksforgeeks.org/operator-overloading-in-python/)