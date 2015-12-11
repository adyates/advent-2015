class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, point):
        return Point(
            self.x + point.x,
            self.y + point.y
        )

    def __eq__(self, point):
        if isinstance (point, Point):
            return point.x == self.x and point.y == self.y
        return False

    def __hash__(self):
        return hash((self.x, self.y))
        
with open('input.txt', 'rb') as f:
    transitions = {
        '^': Point(0, 1),
        '>': Point(1, 0),
        'v': Point(0, -1),
        '<': Point(-1, 0)
    }


    santaPosition = Point(0,0)
    visited = set([santaPosition])
    directions = f.read().strip()

    # For solo Santa
    for direction in directions:
        santaPosition += transitions[direction]
        visited.add(santaPosition)
        
    print 'Visited %s unique positions solo' % len(visited)

    # For Double Santas
    santaPosition = Point(0, 0)
    roboPosition = Point(0, 0)
    visited = set([santaPosition])
    
    for direction in directions[::2]:
        santaPosition += transitions[direction]
        visited.add(santaPosition)
    for direction in directions[1::2]:
        roboPosition += transitions[direction]
        visited.add(roboPosition)

    print 'Visited %s unique positions as a team' % len(visited)
