import random
import pylab
import numpy

def coinFlip(numflips):
    """ Expects a positive int for numFlips """
    head = 0.0
    for i in range(numflips):
        if random.choice(('H','T')) == 'H':
            head += 1
    return head/numflips

def flipSim(numTrials, numFlipsPerTrial) :
    numHeads = []
    for i in range(numTrials):
        numHeads.append(coinFlip(numFlipsPerTrial))
    mean = sum(numHeads)/len(numHeads)
    return mean

def regressToMean(numFlips, numTrails):
    numHeads = []
    for t in range(numTrails):
        numHeads.append(coinFlip(numFlips))
    extremes, nextTrials = [], []
    for i in range(len(numHeads) - 1):
        if numHeads[i] < 0.33 or numHeads[i] > 0.66:
            extremes.append(numHeads[i])
            nextTrials.append(numHeads[i+1])

    pylab.plot(range(len(extremes)), extremes, 'ko', label = 'Extreme')
    pylab.plot(range(len(nextTrials)), nextTrials, 'k^', label = 'Next Trial')
    pylab.axhline(0.5)
    pylab.ylim(0,1)
    pylab.xlim(-1, len(extremes)+1)
    pylab.xlabel('Extreme example and next trials')
    pylab.ylabel('Num heads')
    pylab.title('Regression to mean')
    pylab.legend(loc = 'best')
    pylab.figure()
    pylab.show()

def variance(data):
    mean = sum(data)/len(data)
    tot = 0.0
    for d in data:
        tot += (d - mean)**2
    retrun tot/mean

def stdDev(data):
    return variance(data)**0.05

def flipPlot(minExp, maxExp):
    ratios, diffs, xAxis,stdDiff, stdRatios = [], [], [], [], []
    for exp in range(minExp, maxExp):
        xAxis.append(2**exp)
    
    for numFlips in xAxis:
        numHeads = 0.0
        for i in range(numFlips):
            if random.choice(('H','T')) == 'H':
                numHeads += 1
        numTails = numFlips - numHeads
        diffs.append(abs(numHeads-numTails))
        try:
            if numTails == 0.0:
                ratios.append(1)
            else:
                ratios.append(numHeads/numTails)
        except ZeroDivisionError:
            continue
        
    pylab.title("Diff betweeb head and tails")
    pylab.plot(numpy.log(xAxis), numpy.log(diffs), 'ko')
    pylab.xlabel("Number of flips")
    pylab.ylabel("Diff between head and tails")
    pylab.figure()
    pylab.title("Ratio between head and tails")
    pylab.plot(numpy.log(xAxis), numpy.log(ratios), 'ko')
    pylab.xlabel("Number of flips")
    pylab.ylabel("Ratio of numHeads to numTail")
    pylab.show()


if __name__ == '__main__':
    #print('10 Trials 100 Flips', flipSim(10, 1))
    #regressToMean(15, 40)
    flipPlot(4, 20)