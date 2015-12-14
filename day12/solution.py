import json
import numbers

CHECK_RED = True

with open('input.txt', 'rb') as f:
    dataset = json.loads(f.read().strip())
    inspectionQueue = [dataset]
    dataTotal = 0
    while inspectionQueue:
        current = inspectionQueue.pop()
        if isinstance(current, numbers.Number):
            dataTotal += current
        elif isinstance(current, list):
            inspectionQueue.extend(current)
        elif isinstance(current, dict):
            if CHECK_RED and 'red' in current.values():
                continue
            inspectionQueue.extend(current.values())

    print dataTotal
