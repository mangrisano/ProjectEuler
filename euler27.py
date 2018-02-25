#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divs = math.floor(math.sqrt(n))
    for i in range(3, max_divs + 1, 2):
        if n % i == 0:
            return False
    return True

def problem():
    res = []
    max_count = 0
    for a in list(range(-999, 1000, 2)):
        for b in list(range(-999, 1001)):
            count = 0
            n = 0
            while is_prime(n**2 + a*n + b):
                n += 1
                count += 1
            if count > max_count:
                max_count = count
                res.append([max_count, a * b])
    return max(res)


print(problem())
