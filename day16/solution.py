import re

USE_RANGES = True
PACKAGE_ANALYSIS = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

with open('input.txt', 'rb') as f:
    auntSet = {}
    regex = 'Sue (?P<number>\d+): (?P<data>.*)'
    for line in f.read().strip().split('\n'):
        segment = re.match(regex, line)
        auntSet[segment.group('number')] = {
            item.split(':')[0].strip(): int(item.split(':')[1].strip()) for
            item in segment.group('data').strip().split(',')
        }

    matchingAunts = []
    for auntNumber, traits in auntSet.iteritems():
        fullyMatches = True
        for compound, count in traits.iteritems():
            if USE_RANGES and compound in ['trees', 'cats']:
                fullyMatches = fullyMatches and count > PACKAGE_ANALYSIS[compound]
            elif USE_RANGES and compound in ['pomeranians', 'goldfish']:
                fullyMatches = fullyMatches and count < PACKAGE_ANALYSIS[compound]
            else:
                fullyMatches = fullyMatches and count == PACKAGE_ANALYSIS[compound]
        if fullyMatches:
            matchingAunts.append((auntNumber, traits))
    print matchingAunts
