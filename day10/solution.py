import datetime

SEED = '1113122113'
iterations = 50
def chew(text):
    number = text[0]
    count = 0
    remaining = text

    while remaining and number is remaining[0]:
        count += 1
        remaining = remaining[1:]

    return (number, count, remaining)

text = SEED
startTime = datetime.datetime.now()
while iterations:
    print 'iterations to go: %02d, Time elapsed: %ss' % (
        iterations, (datetime.datetime.now() - startTime).seconds)
    rebuildText = ''
    while text:
        number, count, remaining = chew(text)
        rebuildText += str(count) + number
        text = remaining
    text = rebuildText
    iterations -= 1

print len(text)
