#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: hassanshamim
"""
import ast


def chars_in_file(chars):
    # always longer
    return len(chars)


def chars_in_memory(chars):
    return len(ast.literal_eval(chars))


def encoded_chars(chars):
    extra_slashes = sum(map(chars.count, ('"', '\\')))
    and_quotes = 2
    return len(chars) + extra_slashes + and_quotes


def input_words():
    with open('./day_8.input.txt', 'r') as file:
        for line in file.readlines():
            yield line.strip()


def test_words(flag='r'):
    with open('day_8_test.input', flag) as file:
        for line in file.readlines():

            chars, file_length, memory_length = line.strip().split(b', ' if 'b' in flag else ', ')
            yield chars, file_length, memory_length


def test_v2():
    example_words = [word[0] for word in test_words()]
    expected_results = [6, 9, 16, 11]
    for expected, word in zip(expected_results, example_words):
        result = encoded_chars(word)
        print('Expected Encoded Length of {} to be {}, it was {}'.format(word, expected, result))

        print


def test():
    for word, fl, ml in test_words():
        mem_length = chars_in_memory(word)
        file_length = chars_in_file(word)
        print('Expected File Length of {} to be {}, it was {}'.format(word, fl, file_length))
        print('Expected Memory Length of {} to be {}, it was {}'.format(word, ml, mem_length))


def main():
    total_chars_in_memory = total_chars_in_file = total_chars_encoded = 0
    for word in input_words():
        total_chars_in_file   += chars_in_file(word)
        total_chars_in_memory += chars_in_memory(word)
        total_chars_encoded   += encoded_chars(word)

    print('Result:', total_chars_in_file - total_chars_in_memory)
    print('Second Result: ', total_chars_encoded - total_chars_in_file)


if __name__ == '__main__':
    main()
