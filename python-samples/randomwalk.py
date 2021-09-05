class Location(object):
  def __init__(self, x, y):
    """ x and y  are numbers """
    self.x, self.y = x, y

  def move(self, deltax, deltay):
    """deltax and deltay are numbers"""
    return Location(self.x + deltax, self.y + deltay)

  def getX(self):
    return self.x

  def getY(self):
    return self.y

  def distFrom(self, other):
    ox, oy = other.x, other.y
    xDist, yDist = self.x - ox, self.y - oy
    return (xDist**2 + yDist**2)**0.5

class Field(object):
  def __init__(self):
    self.drunks = {}

  def addDrunk(self, drunk, location):
    if drunk in self.drunks:
      raise ValueError('Duplicate drunk')
    else:
      self.drunks[drunk] = location

  def moveDrunk(self, drunk):
    if drunk not in self.drunks:
      raise ValueError('Drunk not in field')
    xDist, yDist = drunk.takeStep()
    currentLocation = self.drunks[drunk]
    self.drunks[drunk] = currentLocation.move(xDist, yDist)

  def getLoc(self, drunk):
    if drunk not in self.drunks:
      raise ValueError('Drunk not in field')
    return self.drunks[drunk]

class OddField(Field):
  def __init__(self, holes, xRange, yRange):
    Field.__init__(self)
    self.warmholes = {}
    for w in range(holes):
      x = random.randint(-xRange, xRange)
      y = random.randint(-yRange, yRange)
      newX = random.randint(-xRange, xRange)
      newY = random.randint(-yRange, yRange)
      newLoc = Location(newX, newY)
      self.warmholes[(x,y)] = newLoc

  def moveDrunk(self, drunk):
    Field.moveDrunk(self,drunk)
    x = self.drunks[drunk].getX()
    y = self.drunks[drunk].getY()
    if (x,y) in self.warmholes:
      self.drunks[drunk] = self.warmholes[(x,y)]

import random

class Drunk(object):
  def __init__(self, name = None):
    """ Assumes name is a string """
    self.name = name

  def __str__(self):
    if self.name != None:
      return self.name
    return 'Anonymous'

class UsualDrunk(Drunk):
  def takeStep(self):
    stepChoices = [(0,1), (0,-1), (1, 0), (-1,0)]
    return random.choice(stepChoices)

class ColdDrunk(Drunk):
  def takeStep(self):
    stepChoices = [(0.0, 1.0), (0.0, -2.0), (1.0, 0.0), (-1.0,0.0)]
    return random.choice(stepChoices)

class EWDrunk(Drunk):
  def takeStep(self):
    stepChoices = [(1.0, 0.0), (-1.0, 0.0)]
    return random.choice(stepChoices)

class styleIterator(object):
  def __init__(self, styles):
    self.index = 0
    self.styles = styles

  def nextStyle(self):
    result = self.styles[self.index]
    if self.index == len(self.styles) - 1:
      self.index = 0
    else:
      self.index += 1
    return result

def walk(f, d, numSteps):
  """Assumes: f a Field, d a Drunk in f and numSteps an int >= 0
     moves d numSteps times; returns the distance between the
     final location and the start of the walk """
  start = f.getLoc(d)
  for s in range(numSteps):
    f.moveDrunk(d)
  return start.distFrom(f.getLoc(d))

def simWalks(numSteps, numTrials, dClass):
  Homer = dClass()
  origin = Location(0,0)
  distances = []
  for t in range(numTrials):
    f = Field()
    f.addDrunk(Homer, origin)
    distances.append(round(walk(f, Homer, numSteps)))
  return distances

def drunkTest(walkLengths, numTrials, dClass):
  for steps in walkLengths:
    distances = simWalks(steps, numTrials, dClass)
    print(dClass.__name__, 'random walk of ', steps, ' steps')
    print(' Mean = ', round(sum(distances)/len(distances), 4))
    print(' Max = ', max(distances), ' Min = ', min(distances))

def getFinalLocs(numSteps, numTrials, dClass):
  locs = []
  d = dClass()
  for t in range(numTrials):
    f = Field()
    f.addDrunk(d, Location(0,0))
    for s in range(numSteps):
      f.moveDrunk(d)
    locs.append(f.getLoc(d))
  return locs

import pylab
def plotLocs(drunkKinds, numSteps, numTrials):
  styleChoice = styleIterator(('k+', 'r^', 'mo'))
  for dClass in drunkKinds:
    locs = getFinalLocs(numSteps, numTrials, dClass)
    xVals, yVals = [], []
    for loc in locs:
      xVals.append(loc.getX())
      yVals.append(loc.getY())
    meanX = sum(xVals)/len(xVals)
    meanY = sum(yVals)/len(yVals)
    curStyle = styleChoice.nextStyle()
    pylab.plot(xVals, yVals, curStyle, label = dClass.__name__ + ' mean loc = <' + str(meanX) + ', ' + str(meanY))
  pylab.title('Location at End of Walks (' + str(numSteps) + ' steps)')
  pylab.show()

def traceWalk(drunkKinds, numSteps):
  styleChoice = styleIterator(('k+', 'r^', 'mo'))
  #f = Field()
  f = OddField(1000, 100, 200)
  for dClass in drunkKinds:
    d = dClass()
    f.addDrunk(d, Location(0,0))
    locs =  []
    for s in range(numSteps):
      f.moveDrunk(d)
      locs.append(f.getLoc(d))
    xVals, yVals = [],[]
    for l in locs:
      xVals.append(l.getX())
      yVals.append(l.getY())
    curStyle = styleChoice.nextStyle()
    pylab.plot(xVals, yVals, curStyle, label = dClass.__name__)
  pylab.xlabel('Steps East/West of origin')
  pylab.ylabel('steps North/South of origin')
  pylab.legend(loc = 'best')
  pylab.show()

if __name__ == '__main__':
  #drunkTest((10, 100, 1000, 10000), 100, UsualDrunk)
  #drunkTest((10, 100, 1000, 10000), 100, ColdDrunk)
  #drunkTest((10, 100, 1000, 10000), 100, EWDrunk)
  
  #plotLocs((UsualDrunk, ColdDrunk, EWDrunk), 100, 200)

  traceWalk((UsualDrunk, ColdDrunk, EWDrunk), 200)