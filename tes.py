#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)
        yield 5
g = foo()
print('bgin')
print(next(g))
print("*"*20)
print(next(g))
print("*"*20)
print(next(g))