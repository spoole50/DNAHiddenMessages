from pathlib import Path

# Pattern Matching Problem

def patternMatch(pattern, genome):
    res = []
    for i in range(len(genome) - len(pattern) + 1):
        if genome[i:i + len(pattern)] == pattern:
            res.append(i)
    
    print(*res)

#patternMatch("ATAT", "GATATATGCATATACTT")

dataFolder = Path("/mnt/c/Users/shane/Downloads/")
# fileToOpen = dataFolder / "dataset_3_5.txt"
fileToOpen = dataFolder / "Vibrio_cholerae.txt"
with open(fileToOpen) as inFile:
    data = inFile.readlines()

#patternMatch(data[0].strip(), data[1].strip())
patternMatch("CTTGATCAT",data[0].strip())