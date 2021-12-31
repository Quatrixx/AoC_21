from collections import deque
import cProfile
from os import stat
import pstats

def answer_calc(polymer):
    elements = []
    for e in polymer:
        elements.append(e)
    elements.sort()
    elements = {e: elements.count(e) for e in elements}
    elements = sorted(elements.items(), key=lambda e: e[1], reverse=True)
    return(elements[0][1]-elements[-1][1])

with open('day14.in') as input:
    polymer = input.readline().strip()
    input.readline()
    pair_insertion_rules = [ins.strip().split(' -> ') for ins in input.readlines()]
    pair_insertion_rules = {k: v for k, v in pair_insertion_rules}

def do_polymerizsation(polymer, pair_insertion_rules):
    for index in range(len(polymer)-1):
        a = polymer[index+index]
        b = polymer[index+index+1]
        polymer.insert(index+index+1, pair_insertion_rules[a+b])

polymer = deque(polymer)
for step in range(10):
    if step+1 >= 15:
        with cProfile.Profile() as pr:
            do_polymerizsation(polymer, pair_insertion_rules)
        print(f"step {step+1}...")
        stats = pstats.Stats(pr)
        stats.sort_stats(pstats.SortKey.TIME)
        stats.print_stats()
        pass
    else:
        do_polymerizsation(polymer, pair_insertion_rules)
        # part one
        if step+1 == 10:
            print(f"part1: {answer_calc(polymer)}")
        if step+1 == 40:
            print(f"part2: {answer_calc(polymer)}")
