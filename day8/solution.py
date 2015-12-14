import re

with open('input.txt', 'rb') as f:
    charCount = 0
    memCount = 0
    expandCount = 0
    for line in f.read().strip().split('\n'):
        charCount += len(line)
        memCount += len(eval(line))
        trimmed, hexCount = re.subn('\\\\x..', '', line[1:-1].replace('\\\\', 'S'))
        trimmed, escapeCount = re.subn('\\\\.', '', trimmed.replace('S', '\\\\'))
        expandSize = (
            6 +
            len(trimmed) +
            hexCount * 5 +
            escapeCount * 4
        )
        expandCount += expandSize
    print '%s - %s = %s' % (expandCount, charCount, expandCount - charCount)
    print '%s - %s = %s' % (charCount, memCount, charCount - memCount)
