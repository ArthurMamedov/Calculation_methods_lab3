#from math import *
import numpy as np
from functools import lru_cache


class Func:
    def __init__(self, f, d1, d2):
        self.f = f
        self.d1 = d1
        self.d2 = d2


def get_interval(f: 'function', a, b, eps):
    x = a; prev_y = f.f(x)
    while x < b:
        x += eps
        y = f.f(x)
        if y * prev_y <= 0:
            prev_y = y
            yield x - eps, x


def half_division(f: Func, a, b, eps) -> float:
    '''Finds an approximate root of an equation using 'half divesion' method'''
    i = 0
    while True:
        i += 1
        x = (a + b) / 2
        if f.f(a) * f.f(x) < 0:
            b = x
        else:
            a = x
        if abs(f.f((a + b) / 2)) < eps:
            return (a + b) / 2, i


#add different checks here
def simple_iteratiron(f: 'func(x)', a, b, eps) -> float:
    '''Finds an approximate root of an equation with 'simple iteration' method'''
    t, s = a, (b - a) / 500
    while t < b:
        if f.d1(t) * f.d1(t + s) < 0:
            return 'Simple iteration method is not applied because the first derivative changes its sign.', -1
        t += s

    interval = [f.d1(x) for x in np.arange(a, b, (b - a)/500)]
    _min_ = min(interval)
    _max_ = max(interval)
    k = 2 / (_min_ + _max_) * (-1 if f.d1((b - a) / 2) < 0 else 1)
    phi = lambda x: x - (k * f.f(x))
    x1 = (a + b) / 2; i = 0
    while True:
        i += 1
        x0 = x1
        x1 = phi(x0)
        if abs(f.f(x1)) < eps:
            return x1, i


#add then different checks
def tangent(f: 'func(x)', a, b, eps) -> float:
    '''Finds an approximate root of an equation with 'Newton(tangent)' method'''
    t, s = a, (b - a) / 500
    while t < b:
        if f.d1(t) * f.d1(t + s) < 0 or f.d2(t) * f.d2(t + s) < 0:
            return 'Tangent method is not applied because first or second derivatives changes their signes.', -1
        t += s

    x = a if f.f(a) * f.d2(a) > 0 else b; i = 0
    while True:
        i += 1
        if abs(f.f(x)) < eps:
            return x, i
        x -= f.f(x) / f.d1(x)


def chord(f: Func, a, b, eps):
    '''Finds an approximate root of an equation using 'chord' method'''
    t, s = a, (b - a) / 500
    while t < b:
        if f.d1(t) * f.d1(t + s) < 0 or f.d2(t) * f.d2(t + s) < 0:
            return 'Chord method is not applied because first or second derivatives changes their signes.', -1
        t += s

    c = a; x = (a + b) / 2; i = 0
    while c < b:  #in this loop we find 'c'
        if f.f(c) * f.d2(c) > 0:
            break
        c += eps
    while True:
        i += 1
        x = x - ((x - c) * f.f(x)) / (f.f(x) - f.f(c))
        if abs(f.f(x)) < eps:
            return x, i


def combined(f: 'func(x)', a, b, eps):
    t, s = a, (b - a) / 500
    while t < b:
        if f.d1(t) * f.d1(t + s) < 0 or f.d2(t) * f.d2(t + s) < 0:
            return 'Combined method is not applied because first or second derivatives changes their signes.', -1
        t += s

    i = 0
    while True:
        i += 1
        if f.f(a) * f.d2(a) < 0:
            a = a - f.f(a) * (a - b) / (f.f(a) - f.f(b))
        else:
            a = a - f.f(a) / f.d1(a)
        if f.f(b) * f.d2(b) < 0:
            b = b - f.f(b) * (b - a) / (f.f(b) - f.f(a))
        else:
            b = b - f.f(b) / f.d1(b)
        if abs(f.f((a + b) / 2)) <= eps:
            return (a + b) / 2, i
