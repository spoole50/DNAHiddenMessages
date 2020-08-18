def symToNum(symbol):
    symMap = {'A': 0,
              'C': 1,
              'G': 2,
              'T': 3}
    return symMap[symbol]

def numToSym(num):
    numMap = {0: 'A',
              1: 'C',
              2: 'G',
              3: 'T'}
    return numMap[num]

def numToPat(index, k):
    if k == 1:
        return numToSym(index)
    pfixIndex = int(index / 4)
    r = index % 4
    sym = numToSym(r)
    pfixPattern = numToPat(pfixIndex, k - 1)
    return pfixPattern + sym

def patToNum(pattern):
    if not pattern:
        return 0
    symbol = pattern[-1]
    prefix = pattern[:-1]
    return 4 * patToNum(prefix) + symToNum(symbol)

def computeFreq(text, k):
    freq = [0] * (4 ** k)
    for i in range(len(text) - k + 1):
        pat = text[i:i + k]
        j = patToNum(pat)
        freq[j] += 1
    return freq

#print(patToNum("TTAGCTGAGCTCCCTCA"))
#print(numToPat(7601, 10))
#print(computeFreq("ACGCGGCTCTGAAA", 2))

from pathlib import Path

dataFolder = Path("/mnt/c/Users/shane/Documents/Coursera/DNA_HiddenMessages/Week1/")
fileToOpen = dataFolder / "dataset_2994_5.txt"
with open(fileToOpen) as inFile:
    data = inFile.readlines()

import sys
fileToW = dataFolder / "res.txt"
f = open(fileToW, 'w')
print(*computeFreq(data[0].strip(), int(data[1].strip())),sep=' ', file=f)
f.close()