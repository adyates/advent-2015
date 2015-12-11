import md5

SECRET_KEY = 'bgvyzdsv'

magicNumber = 0
magicDigest = md5.new(SECRET_KEY + str(magicNumber)).hexdigest()

while ('00000' != magicDigest[:5]):
    magicNumber += 1
    magicDigest = md5.new(SECRET_KEY + str(magicNumber)).hexdigest()

print '%s yields %s' % (magicNumber, magicDigest)

while ('000000' != magicDigest[:6]):
    magicNumber += 1
    magicDigest = md5.new(SECRET_KEY + str(magicNumber)).hexdigest()

print '%s yields %s' % (magicNumber, magicDigest)
