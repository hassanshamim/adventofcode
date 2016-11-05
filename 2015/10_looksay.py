#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: hassanshamim
"""
from itertools import groupby



def looksay(num):
    """takes int, returns int after looksay conversion"""
    if isinstance(num, int):
        num = str(num)
    num_counts = (str(sum(1 for _ in g))+ k for k,g in groupby(num))
    return ''.join(num_counts)

    
def main():
    result = start =  1113122113
    for i in range(50):
        result = looksay(result)
    print(len(str(result)))

if __name__ == '__main__':
    main()
