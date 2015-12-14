import re

def parseInstruction(text):
    return re.match(
        '(?P<cmd>.*) (?P<startX>\d+),(?P<startY>\d+) through (?P<endX>\d+),(?P<endY>\d+)', text)

def lightCount(lightGrid):
    return reduce(lambda x, y: x + y, [light for row in lightGrid for light in row], 0)

with open('input.txt', 'rb') as f:
    ops = {
        'toggle': lambda x: x + 2,
        'turn on': lambda x: x + 1,
        'turn off': lambda x: max(x - 1, 0),
    }

    lightGrid = [[0 for x in range(1000)] for y in range(1000)]
    for instruction in f.readlines():
        match = parseInstruction(instruction)
        for xIndex in range(int(match.group('startX')), int(match.group('endX')) + 1):
            for yIndex in range(int(match.group('startY')), int(match.group('endY')) + 1):
                lightGrid[xIndex][yIndex] = ops[match.group('cmd')](lightGrid[xIndex][yIndex])

    count = lightCount(lightGrid)
    print 'There are %s lights on' % count
