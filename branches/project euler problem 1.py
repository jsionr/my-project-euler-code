#!/usr/bin/env python
# -*- coding: utf-8 -*-

sum(list(set([i for i in range(1000) if not i%3 or not i%5 ])))