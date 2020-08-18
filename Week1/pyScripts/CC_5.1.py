from pathlib import Path

# Cylce through the cordinates checking if there are at least t occurances in any given window
def checkWindow(cords, L, t, gLen):
    for i in range(len(cords) - 1):
        tmp = 1
        start = cords[i][0]
        while i + 1 < len(cords) and cords[i + 1][1] <= start + L:
            tmp += 1
            i += 1
        if tmp >= t:
            return True
    return False

def clumpy(genome, k, L, t):
    allKs = []
    kmerDict = dict()
    # Build Dictionary of all k-mers in genome, saving the start and stop coordinates for each
    for i in range(k, len(genome) - k + 1):
        kmer = genome[i - k:i]
        if kmer not in kmerDict:
            kmerDict[kmer] = [(i - k, i)]
        else:
            kmerDict[kmer].append((i - k, i))
    # Cycle through the dictionary and if a kmer appears at least t times in genome check if it occurs t time in any given L window
    for kmer in kmerDict:
        if len(kmerDict[kmer]) >= t:
            if checkWindow(kmerDict[kmer], L, t, len(genome)):
                allKs.append(kmer)
    print (len(allKs))
            
#clumpy("CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA", 5, 50, 4)

dataFolder = Path("/mnt/c/Users/shane/Documents/Coursera/DNA_HiddenMessages/Week1/")
fileToOpen = dataFolder / "E_coli.txt"
with open(fileToOpen) as inFile:
    data = inFile.readlines()

clumpy(data[0].strip(), 9, 500, 3)