import re

class Reindeer(object):

    def __init__(self, name, speed, flyTime, restTime):
        self.name = name
        self.speed = speed
        self.flyTime = flyTime
        self.restTime = restTime

        self.isFlying = True
        self.timeRemaining = flyTime
        self.distance = 0
        self.points = 0

    def __str__(self):
        return '%s has gone %s km, has %s points, and is %s.' % (
            self.name, self.distance, self.points, 'flying' if self.isFlying else 'resting')

    def __cmp__(self, other):
        assert isinstance(other, Reindeer)
        return self.points - other.points

    def nextTick(self):
        self.timeRemaining -= 1
        if self.isFlying:
            self.distance += self.speed
        if self.timeRemaining <= 0:
            self.isFlying = not self.isFlying
            self.timeRemaining = self.flyTime if self.isFlying else self.restTime

    def addPoint(self):
        self.points += 1


RACE_TIME = 2503
with open('input.txt', 'rb') as f:
    stable = []
    regex = (
        '(?P<reindeer>.*) can fly (?P<speed>\d+) km/s for (?P<flyTime>\d+)'
        ' seconds, but then must rest for (?P<restTime>\d+) seconds.'
    )
    for line in f.read().strip().split('\n'):
        segment = re.match(regex, line)
        reindeer = Reindeer(segment.group('reindeer'), int(segment.group('speed')),
            int(segment.group('flyTime')), int(segment.group('restTime')))
        stable.append(reindeer)

    timeRemaining = RACE_TIME
    while timeRemaining:
        timeRemaining -= 1
        [reindeer.nextTick() for reindeer in stable]

        leadDistance = 0
        leaders = []
        for reindeer in stable:
            if reindeer.distance > leadDistance:
                leadDistance = reindeer.distance
                leaders = [reindeer]
            elif reindeer.distance == leadDistance:
                leaders.append(reindeer)
        [reindeer.addPoint() for reindeer in leaders]

    print '==============='
    for reindeer in stable:
        print reindeer
