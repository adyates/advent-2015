import itertools
import re
import sys

with open('input.txt', 'rb') as f:
    mapping = {}
    worlds = set([])
    regex = '(?P<pointA>.*) to (?P<pointB>.*) = (?P<distance>\d+)'
    for line in f.read().strip().split('\n'):
        segment = re.match(regex, line)
        endpoints = (segment.group('pointA'), segment.group('pointB'))
        distance = int(segment.group('distance'))
        mapping[(endpoints[0], endpoints[1])] = distance
        mapping[(endpoints[1], endpoints[0])] = distance
        worlds.add(endpoints[0])
        worlds.add(endpoints[1])

    minPath = []
    minCost = sys.maxint

    maxPath = []
    maxCost = 0

    for sequence in itertools.permutations(worlds):
        thisCost = 0
        for index in range(len(sequence) - 1):
            thisCost += mapping[(sequence[index], sequence[index + 1])]
        if minCost > thisCost:
            minCost = thisCost
            minPath = sequence
        if maxCost < thisCost:
            maxCost = thisCost
            maxPath = sequence

    print 'The shortest path takes %s: %s' % (minCost, minPath)
    print 'The longest path takes %s: %s' % (maxCost, maxPath)
