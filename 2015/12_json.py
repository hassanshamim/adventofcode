""""
--- Day 12: JSAbacusFramework.io ---

Santa's Accounting-Elves need help balancing the books after a recent order. Unfortunately, their accounting software uses a peculiar storage format. That's where you come in.

They have a JSON document which contains a variety of things: arrays ([1,2,3]), objects ({"a":1, "b":2}), numbers, and strings. Your first job is to simply find all of the numbers throughout the document and add them together.

For example:

    [1,2,3] and {"a":2,"b":4} both have a sum of 6.
    [[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
    {"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
    [] and {} both have a sum of 0.
    You will not encounter any strings containing numbers.

    What is the sum of all numbers in the document?
"""


import json


def crawl_dict(data):
    for val in data.values():
        if isinstance(val, int):
            yield val
        elif isinstance(val, list):
            yield from crawl_list(val)
        elif isinstance(val, dict):
            yield from crawl_dict(val)


def crawl_list(data):
    for val in data:
        if isinstance(val, int):
            yield val
        elif isinstance(val, list):
            yield from crawl_list(val)
        elif isinstance(val, dict):
            yield from crawl_dict(val)


def crawl_dict_no_red(data):
    #import ipdb; ipdb.set_trace()
    if not ('red' in data.keys() or 'red' in data.values()):
        for val in data.values():
            if isinstance(val, int):
                yield val
            elif isinstance(val, list):
                yield from crawl_list(val)
            elif isinstance(val, dict):
                yield from crawl_dict_no_red(val)


if __name__ == '__main__':

    with open('./day_12.input.txt', 'r') as f:
        data = json.load(f)

    print('Sum is: ', sum(crawl_dict(data)))
    crawl_dict = crawl_dict_no_red # for part 2
    print('Sum no red is:', sum(crawl_dict(data)))
