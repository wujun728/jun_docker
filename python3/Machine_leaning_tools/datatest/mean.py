
from numpy import *
import sys

def loadset(filename,n,splittype):
    fr = open(filename)
    datamat = []
    i = int(n)
    sums = 0.0
    n = 0
    for line in fr.readlines():
        lines = line.strip().split(splittype)
        sums = sums + float(lines[i-1])
        n = n+1
    return sums,n

def test(filename,n,splittype):
    print splittype
    sums,n = loadset(filename,n,splittype)
    average = sums/n
    print 'mean is : ' + str(average)

if __name__ == "__main__":
	if sys.argv[3] == "\\t":
		test(sys.argv[1],int(sys.argv[2]),"\t")


