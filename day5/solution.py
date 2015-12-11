import re

def hasRepeats(text):
    nextLetters = text[1:]
    for index in range(len(nextLetters)):
        if text[index] == nextLetters[index]:
            return text[index:index+2]
    return ''

def hasDoubleRepeats(text):
    nextLetters = text[1:]
    nextPair1 = text[2:]
    nextPair2 = text[3:]
    for index in range(len(nextPair2)):
        if text[index] == nextLetters[index]:
            return True
    return False

def basicNiceness(text):
    return (len(re.findall('[aeiou]', line)) >= 3 and
        hasRepeats(line) and
        not re.match('.*(ab|cd|pq|xy).*', line))

def advNiceness(text):
    pass

with open('input.txt', 'rb') as f:
    niceStringCount = 0

    for line in f.read().split('\n'):
        if basicNiceness(line):
            niceStringCount += 1

    print niceStringCount
