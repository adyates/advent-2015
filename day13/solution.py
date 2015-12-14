import itertools
import re
import sys

INCLUDE_TETSUJIN = True
with open('input.txt', 'rb') as f:
    mapping = {}
    people = set([])
    regex = (
        '(?P<personA>.*) would (?P<sign>.*) (?P<points>\d+) happiness units by '
        'sitting next to (?P<personB>.*).'
    )
    for line in f.read().strip().split('\n'):
        segment = re.match(regex, line)
        seating = (segment.group('personA'), segment.group('personB'))
        happiness = (1 if segment.group('sign') == 'gain' else -1) * int(segment.group('points'))
        mapping[seating] = happiness
        people.add(seating[0])
        people.add(seating[1])

    if INCLUDE_TETSUJIN:
        for guest in people:
            mapping[('Tetsujin', guest)] = 0
            mapping[(guest, 'Tetsujin')] = 0
        people.add('Tetsujin')

    sadSeating = []
    minSmiles = sys.maxint

    gladSeating = []
    maxSmiles = 0

    for sequence in itertools.permutations(people):
        thisCost = mapping[(sequence[0], sequence[-1])] + mapping[(sequence[-1], sequence[0])]
        for index in range(len(sequence) - 1):
            thisCost += (
                mapping[(sequence[index], sequence[index + 1])] +
                mapping[(sequence[index + 1], sequence[index])]
            )
        if minSmiles > thisCost:
            minSmiles = thisCost
            sadSeating = sequence
        if maxSmiles < thisCost:
            maxSmiles = thisCost
            gladSeating = sequence

    print 'The saddest arrangement is %s: %s' % (minSmiles, sadSeating)
    print 'The happiest arrangement is %s: %s' % (maxSmiles, gladSeating)
