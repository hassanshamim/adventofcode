#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

For example:

turn on 0,0 through 999,999 would turn on (or leave on) every light.
toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.

--- Part Two ---

You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of those lights by 1.

The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?
"""

import numpy as np


def decompose(line):
    words = line.split()
    if len(words) == 5:
        words = words[1:]

    msg, start, _, stop =  words
    start = (int(i) for i in start.split(','))
    stop = (int(i)+1 for i in stop.split(',')) # add one for python ranges
    x_slice, y_slice = map(slice, start, stop)

    return msg, x_slice, y_slice

def toggle(x_slice, y_slice):
    global lights
    lights[x_slice, y_slice] = 1 - lights[x_slice, y_slice]

def toggle2(x_slice, y_slice):
    global lights
    lights[x_slice, y_slice] += 2

def turn_on(x_slice, y_slice):
    global lights
    lights[x_slice, y_slice] =  1

def turn_on2(x_slice, y_slice):
    global lights
    lights[x_slice, y_slice] += 1

def turn_off(x_slice, y_slice):
    global lights
    lights[x_slice, y_slice] = 0

def turn_off2(x_slice, y_slice):
    global lights
    lights[x_slice, y_slice] = (lights[x_slice, y_slice] - 1).clip(min=0)

def input_lines():
    with open('./day_6.input', 'r') as file:
        for line in file.readlines():
            yield line


if __name__ == '__main__':

    lights = np.zeros((1000,1000))
    instructions = {'toggle': toggle, 'off': turn_off, 'on': turn_on}

    for line in input_lines():
        directive, xs, ys = decompose(line)
        func = instructions[directive]
        func(xs, ys)

    print('total lights left on:', lights.sum())
