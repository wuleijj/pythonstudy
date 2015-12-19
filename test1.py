import math


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type.')

    if x >= 0:
        return x
    else:
        return -x


def nop():
    pass


def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

def power(x, n=2):
    return x ** n

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum
