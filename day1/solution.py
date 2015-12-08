with open('input.txt', 'rb') as f:
  transitions = {
    '(': 1,
    ')': -1
  }
  currentFloor = 0
  transitionCount = 0
  for movement in f.read().strip():
    currentFloor += transitions[movement]
    transitionCount += 1
    if currentFloor is -1:
      print 'Hit Bastment floor after %s transitions' % transitionCount
  print 'Final floor: %s' % currentFloor
