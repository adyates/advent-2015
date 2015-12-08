with open('input.txt', 'rb') as f:
  totalPaper = 0
  totalRibbon = 0

  for line in f:
      length, width, height = [int(dim) for dim in line.strip().split('x')]
      dimensions = sorted([length, width, height])

      box = 2*(length * width + width * height + length * height)
      slack = dimensions[0] * dimensions[1]
      ribbonWrap = 2 * (dimensions[0] + dimensions[1])
      ribbonBow = length * width * height

      totalPaper += box + slack
      totalRibbon += ribbonWrap + ribbonBow

  print 'Total wrapping paper required: %s' % totalPaper
  print 'Total ribbon required: %s' % totalRibbon
