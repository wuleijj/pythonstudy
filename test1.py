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

a = float(input('please input a = '))
b = float(input('please input b = '))
c = float(input('please input c = '))

def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError('bad operand type.')
    if not isinstance(b, (int, float)):
        raise TypeError('bad operand type.')    
    if not isinstance(c, (int, float)):
        raise TypeError('bad operand type.')

    k=math.sqrt(float(b*b-4*a*c))
    if a==0:
        x=(-b)/c
        return x
    elif k>=0:
        x1=(-b+k)/(2*a)
        x2=(-b-k)/(2*a)
        return x1,x2
    else:
        return '方程无实数解'

print(quadratic(a,b,c))
