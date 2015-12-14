CURRENT_PASSWORD = 'hepxxyzz'

class SantaPassword(object):

    MAX_CHAR = ord('z')
    MIN_CHAR = ord('a')

    def __init__(self, text):
        self.password = [ord(letter) for letter in text]

    def __str__(self):
        return ''.join([chr(letter) for letter in self.password])

    def hasRunRequirement(self):
        for index in range(len(self.password) - 2):
            triplet = self.password[index:index + 3]
            if (triplet[0] + 1 == triplet[1] and triplet[1] + 1 == triplet[2]):
                return True
        return False

    def hasInvalidChars(self):
        INVALID_CHARS = [ord(invalid) for invalid in 'iol']
        for char in self.password:
            if char in INVALID_CHARS:
                return True
        return False

    def hasTwoPairs(self):
        pairSet = set([])
        for index in range(len(self.password) - 1):
            pair = self.password[index:index + 2]
            if (pair[0] == pair[1]):
                pairSet.add(pair[0])
        return len(pairSet) >= 2

    def nextPassword(self):
        self.password[7] += 1
        for index in range(len(self.password) - 1, -1, -1):
            if self.password[index] > self.MAX_CHAR:
                self.password[index] = self.MIN_CHAR
                self.password[index - 1] += 1
            else:
                break

    def isValid(self):
        return self.hasRunRequirement()  and self.hasTwoPairs() and not self.hasInvalidChars()

santaPass = SantaPassword(CURRENT_PASSWORD)
santaPass.nextPassword()

while not santaPass.isValid():
    santaPass.nextPassword()

print santaPass
