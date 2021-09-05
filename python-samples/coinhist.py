import pylab
import random

def variance(data):
    """ Assumes that an array of integers is passed """
    mean = sum(data)/len(data)
    tot = 0.0
    for d in data:
        tot += (d - mean)**2
    return tot/mean

def stdDev(data):
    """ Assumes that an array of integers is passed """
    return variance(data)**0.5

def coinFlip(numFlips):
    numHeads = 0
    for i in range(numFlips):
        if random.choice(('H', 'T')) == 'H':
            numHeads += 1
    return numHeads/float(numFlips)

def runTrials(numFlips, numTrials):
    headRatio = []
    for i in range(numTrials):
        headRatio.append(coinFlip(numFlips))
    mean = sum(headRatio)/len(headRatio)
    stddev = stdDev(headRatio)
    return (headRatio, mean, stddev)

def labelPlots(numFlips, numTrials, mean, stddev):
    pylab.title(str(numTrials) + ' trails of '+ str(numFlips)+ ' each ')
    pylab.xlabel('Fraction of heads')
    pylab.ylabel('Number of trails')
    pylab.annotate('Mean = '+ str(round(mean,4))\
        + '\nSD = '+ str(round(stddev,4)), size = 'x-large',
        xycoords = 'axes fraction', xy = (0.67, 0.5))

def coinHist(numFlips, numTrials):
    headRatio, mean, stddev = runTrials(numFlips, numTrials)
    pylab.hist(headRatio, bins = 20)
    xmin, xmax = pylab.xlim()
    labelPlots(numFlips, numTrials, mean, stddev)
    return xmin, xmax

if __name__ == '__main__':
    xmin, xmax = coinHist(100, 100000)
    pylab.figure()
    pylab.xlim(xmin, xmax)
    coinHist(1000, 100000)
    pylab.show()