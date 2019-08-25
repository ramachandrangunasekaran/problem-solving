#!/bin/python

import math
import os
import random
import re
import sys


def buy_container(a, b):
    return a / b


def find_total_containers(n, inputs):
    for input in inputs:
        pricing_slab = map(int, input.split(' '))
        # newly bought & emptied containers
        empty_containers = total_containers = buy_container(pricing_slab[0], pricing_slab[1])
        while empty_containers >= pricing_slab[2]:
            # replacement containers
            new_containers = buy_container(empty_containers, pricing_slab[2])
            empty_containers = new_containers + (empty_containers % pricing_slab[2])
            total_containers += new_containers
        print(total_containers)
    return True


if __name__ == '__main__':
    data = sys.stdin.readlines()
    input_count = data[0]
    inputs = []
    for line in data[1:]:
        inputs.append(line)

    find_total_containers(input_count, inputs)
