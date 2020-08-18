from pathlib import Path

def FrequentWords(text, k, ret_max=True):
    patterns = dict()
    maxCount = 0
    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        if kmer not in patterns:
            patterns[kmer] = 1
        else:
            patterns[kmer] += 1
            if patterns[kmer] > maxCount:
                maxCount = patterns[kmer]
    if ret_max == False:
        return patterns
    
    else:
        res = []
        for kmer in patterns:
            if patterns[kmer] == maxCount:
                res.append(kmer)
        return res

FrequentWords("CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT", 3)
# dataFolder = Path("/mnt/c/Users/shane/Downloads/")
# fileToOpen = dataFolder / "dataset_2_10.txt"
# with open(fileToOpen) as inFile:
#     data = inFile.readlines()

# FrequentWords(data[0].strip(), int(data[1].strip()))