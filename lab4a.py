#!/usr/bin/env python3

def join_sets(s1, s2):
    return s1 | s2  # union of both sets

def match_sets(s1, s2):
    return s1 & s2  # intersection of both sets

def diff_sets(s1, s2):
    return s1 ^ s2  # symmetric difference (non-shared)

if __name__ == '__main__':
    set1 = set(range(1,10))
    set2 = set(range(5,15))
    print('set1: ', set1)
    print('set2: ', set2)
    print('join: ', join_sets(set1, set2))
    print('match: ', match_sets(set1, set2))
    print('diff: ', diff_sets(set1, set2))
