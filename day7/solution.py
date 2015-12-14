import re

class CircuitElement(object):
    wireMap = {}
    matcher = ''

    def didCompute(self):
        return self.output in self.wireMap

    def compute(self):
        raise NotImplementedError()

    def canCompute(self):
        raise NotImplementedError()

    def hasValue(self, wire):
        return isinstance(wire, int) or wire in self.wireMap

    def getValue(self, wire):
        return wire if isinstance(wire, int) else self.wireMap.get(wire)


class Inverter(CircuitElement):

    matcher = 'NOT (?P<input>.*) -> (?P<output>.*)'

    def __init__(self, instruction):
        m = re.match(self.matcher, instruction)
        wire = m.group('input')
        output = m.group('output')

        self.input = int(wire) if wire.isdigit() else wire
        self.output = int(output) if output.isdigit() else output

    def canCompute(self):
        return self.hasValue(self.input)

    def compute(self):
        self.wireMap[self.output] = ~self.getValue(self.input)


class Assignment(CircuitElement):

    matcher = '(?P<input>.*) -> (?P<output>.*)'

    def __init__(self, instruction):
        m = re.match(self.matcher, instruction)
        wire = m.group('input')
        output = m.group('output')

        self.input = int(wire) if wire.isdigit() else wire
        self.output = int(output) if output.isdigit() else output

    def canCompute(self):
        return self.hasValue(self.input)

    def compute(self):
        self.wireMap[self.output] = self.getValue(self.input)


class LogicGate(CircuitElement):

    def __init__(self, instruction):
        m = re.match(self.matcher, instruction)
        input1 = m.group('input1')
        input2 = m.group('input2')
        output = m.group('output')

        self.input1 = int(input1) if input1.isdigit() else input1
        self.input2 = int(input2) if input2.isdigit() else input2
        self.output = int(output) if output.isdigit() else output

    def canCompute(self):
        return self.hasValue(self.input1) and self.hasValue(self.input2)


class LogicalAnd(LogicGate):

    matcher = '(?P<input1>.*) AND (?P<input2>.*) -> (?P<output>.*)'

    def compute(self):
        self.wireMap[self.output] = self.getValue(self.input1) & self.getValue(self.input2)


class LogicalOr(LogicGate):

    matcher = '(?P<input1>.*) OR (?P<input2>.*) -> (?P<output>.*)'

    def compute(self):
        self.wireMap[self.output] = self.getValue(self.input1) | self.getValue(self.input2)


class LogicalLShift(LogicGate):

    matcher = '(?P<input1>.*) LSHIFT (?P<input2>.*) -> (?P<output>.*)'

    def compute(self):
        self.wireMap[self.output] = self.getValue(self.input1) << self.getValue(self.input2)


class LogicalRShift(LogicGate):

    matcher = '(?P<input1>.*) RSHIFT (?P<input2>.*) -> (?P<output>.*)'

    def compute(self):
        self.wireMap[self.output] = self.getValue(self.input1) >> self.getValue(self.input2)


if __name__ == '__main__':
    with open('input.txt', 'rb') as f:
        elements = []
        logicGateMap = {
            'AND': LogicalAnd,
            'OR': LogicalOr,
            'LSHIFT': LogicalLShift,
            'RSHIFT': LogicalRShift
        }

        # Parse lines
        for line in f.read().strip().split('\n'):
            tokens = line.split(' ')
            if len(tokens) == 3:
                elements.append(Assignment(line))
            elif len(tokens) == 4:
                elements.append(Inverter(line))
            else:
                elements.append(logicGateMap[tokens[1]](line))

        # Prune until all completed
        def convergeCircuit():
            completedElements = 0
            while (completedElements < len(elements)):
                print 'Elements completed: %s' % completedElements
                completedElements = len(
                    [element.compute() for element in elements if
                        element.canCompute()])
            print CircuitElement.wireMap
            print CircuitElement.wireMap['a']

        convergeCircuit()

        # Find and override b with a
        for element in elements:
            if isinstance(element, Assignment) and element.output == 'b':
                element.input = CircuitElement.wireMap['a']
        CircuitElement.wireMap.clear()
        convergeCircuit()
