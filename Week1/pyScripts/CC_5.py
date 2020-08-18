from pathlib import Path
from CC_2 import FrequentWords

allKs = set()
def clumpFind(genome, k, L, t):
    end = L
    while True:
        tmpKs = FrequentWords(genome[(end-L):end], k, False)
        for kmer in tmpKs:
            if tmpKs[kmer] >= t:
                allKs.add(kmer)
        if end == len(genome) - 1:
            break
        else:
            end += 1
    print(allKs)

clumpFind("CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA", 5, 50, 4)

# dataFolder = Path("/mnt/c/Users/shane/Documents/Coursera/DNA_HiddenMessages/Week1")
# # fileToOpen = dataFolder / "dataset_4_5.txt"
# fileToOpen = dataFolder / "E_coli.txt"
# with open(fileToOpen) as inFile:
#     data = inFile.readlines()

# # nums = data[1].split(" ")
# # clumpFind(data[0].strip(), int(nums[0].strip()), int(nums[1].strip()), int(nums[2].strip()))

# clumpFind(data[0].strip(), 9, 500, 3)