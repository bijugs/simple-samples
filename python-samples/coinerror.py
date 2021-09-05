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

def showErrorBars(minFlips, maxFlips, numTrials):
    means, sds, xVals = [],[],[]
    for i in range(minFlips, maxFlips+1):
        xVals.append(2**i)
        ratio, mean, stddev = runTrials(2**i, numTrials)
        means.append(mean)
        sds.append(stddev)
    print(means)
    print(sds)
    print(1.96*pylab.array(sds))
    pylab.errorbar(xVals, means, yerr = 1.96*pylab.array(sds))
    pylab.semilogx()
    pylab.show()

if __name__ == '__main__':
    showErrorBars(2,10,10)

