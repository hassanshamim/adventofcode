#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9

@author: Hassan Shamim

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
ugknbfddgicrmopn - nice
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.


--- Part Two ---

Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the string
 without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them, like xyx,
abcdefeghi (efe), or even aaa.
"""

import re #ugh
from itertools import tee

def pairwise(iterable):
    "abcde -> (a,b), (b,c), (c,d), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def nice1(given_word):

    has_forbidden = any(chars in given_word for chars in ('ab','cd','pq','xy'))
    vowel_count = sum(given_word.count(v) for v in 'aeiou')
    no_repeats = not any(a == b for a, b in pairwise(given_word))

    if has_forbidden or (vowel_count < 3) or no_repeats:
        return False
    return True

def nice2(given_word):
    reg1 = re.search(r'(\w)\w\1', given_word)
    reg2 = re.search(r'(\w{2}).*\1', given_word)

    if reg1 and reg2:
        return True
    return False

def input_words():
    with open('./day_5.input', 'r') as file:
        for line in file.readlines():
            yield line

if __name__ == '__main__':
    total1 = sum(map(nice1, input_words()))
    total2 = sum(map(nice2, input_words()))
    print('Number of nice1 strings are:', total1)
    print('Number of nice2 strings are:', total2)
