#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
--- Day 11: Corporate Policy ---

Santa's previous password expired, and he needs help choosing a new one.

To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons), so he finds his new password by incrementing his old password string repeatedly until it is valid.

Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one step; if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.

Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:

Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz."""

import re

TRIPS = ('abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'pqr', 'qrs', 'rst', 'stu',
         'tuv', 'uvw', 'vwx', 'wxy', 'xyz')
VALID = 'abcdefghjkmnpqrstuvwxyz'
FORBIDDEN = {'i', 'o', 'l'}
regex = re.compile(r'(\w)\1')


def rule_one(pw):
    """
    >>> rule_one('hijklmmn')
    False
    """
    return any(trip in pw for trip in TRIPS)


def rule_two(pw):
    return True  # I deal with this in TRIPS and increment()


def rule_three(pw):
    result = regex.findall(pw)
    if len(result) == 2:
        return result[0] != result[1]  # are the duplicates different?
    return False


def increment(word):
    if not word:
        return ''

    head, tail = word[0], word[1:]

    if set(tail) == set('z'):
        return increment_char(head) + len(tail) * 'a'
    elif not tail:
        return increment_char(head)
    else:
        return head + increment(tail)


def increment_char(char):
    if len(char) > 1:
        raise TypeError('Expected a single character, not:  {}'.format(char))
    i = VALID.find(char) + 1
    i = i % len(VALID)
    return VALID[i]


def next_password(pw):
    while True:
        pw = increment(pw)
        if valid(pw):
            break
    return pw


def valid(pw):
    return rule_one(pw) and rule_two(pw) and rule_three(pw)
    
def next_word(pw):
    ''' if input word is not valid, calculate the next valid word by rule 2.
        Not necessarily a valid password
    '''
    if not any(char in pw for char in FORBIDDEN):
        return pw
        
    replacements = {'i': 'j', 'o': 'p', 'l': 'm'}
    for char in replacements:
        i = pw.find(char)
        if i == -1:
            continue
        pw = pw[:i] + replacements[pw[i]] +  'a' * len(pw[i+1:])
    return pw
    


def main():
    from sys import argv
    if len(argv) == 2:
        start_pw = argv[1]
    else:
        start_pw = 'hepxcrrq'
    
    if not valid(start_pw):
        start_pw = next_word(start_pw)
    
    new_pw = next_password(start_pw)
    print('New valid password is:', new_pw)


if __name__ == '__main__':
    main()
    #import doctest     BOOO
    #octest.testmod()   SPYDER