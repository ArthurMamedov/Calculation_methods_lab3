from modules import *
from math import *
import sympy as sp
import time

#my functions
#first:  x**3 + 3 * x - 1  roots: 0.3222
#second: 3**x - x - 7      roots: 2, -7

x = sp.Symbol('x')

formula = input("Enter the formula: ")
a = float(input('Enter a: '))
b = float(input('Enter b: '))
eps = float(input('Enter the precision: '))
step = float(input('Enter a step for root checking: '))

#finding derivatives
form = formula.replace('sp.', '')
func = lambda x: eval(form.replace('x', f'({x})'))
f_diff = str(eval(f'sp.diff({formula})')) 
d1 = lambda x: eval(f_diff.replace('x', f'({x})'))
s_diff = str(eval(f'sp.diff(sp.diff({formula}))'))
d2 = lambda x: eval(s_diff.replace('x', f'({x})'))
f = Func(func, d1, d2)



#the main program
check = False
for t in get_interval(f, a, b, step):
    check = True
    print('Interval is {}'.format(t))
    print('Half division method: {}, iterations: {}'.format(*half_division(f, *t, eps)))
    print('Simple iteration method: {}, iterations: {}'.format(*simple_iteratiron(f, *t, eps)))
    print('Newton (tangent) method: {}, iterations: {}'.format(*tangent(f, *t, eps)))
    print('Chord method: {}, iterations: {}'.format(*chord(f, *t, eps)))
    print('Combined method: {}, iterations: {}'.format(*combined(f, *t, eps)))
    print('------------------------------------------------------------------------------------')
if not check:
    print(f'There are no roots in the interval [{a}, {b}]')
