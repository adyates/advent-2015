import re

def hasRepeats(text):
    repeatStarts = []
    nextLetters = text[1:]
    for index in range(len(nextLetters)):
        if text[index] == nextLetters[index]:
            repeatStarts.append(index)
    return repeatStarts

def hasDoubleRepeats(text):
    for start in range(len(text) - 2):
        if text[start:start + 2] in text[start + 2:]:
            return True
    return False

def hasHalfTurn(text):
    repeatStarts = []
    nextLetters = text[2:]
    for index in range(len(nextLetters)):
        if text[index] == nextLetters[index]:
            repeatStarts.append(index)
    return repeatStarts

def basicNiceness(text):
    return (len(re.findall('[aeiou]', line)) >= 3 and
        hasRepeats(line) and
        not re.match('.*(ab|cd|pq|xy).*', line))

def advNiceness(text):
    return hasDoubleRepeats(text) and hasHalfTurn(text)

with open('input.txt', 'rb') as f:
    niceStringCount = 0
    nicerStringCount = 0
    
    for line in f.read().split('\n'):
        if basicNiceness(line):
            niceStringCount += 1
        if advNiceness(line):
            print line
            nicerStringCount += 1
            
    print 'There are %s nice strings' % niceStringCount
    print 'But there are %s nicer strings' % nicerStringCount
    
