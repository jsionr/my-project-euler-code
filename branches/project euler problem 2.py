#!/usr/bin/env python
# -*- coding: utf-8 -*-


a=[1,2,3,5,8,13,21,34,55,89]
while a[-1]+a[-2]&lt;4000000:
    a.append(a[-1]+a[-2])
sum([i for i in a if not i%2])