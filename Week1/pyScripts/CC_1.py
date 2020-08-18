from pathlib import Path

def PatternCount(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            count += 1
    return count

dataFolder = Path("/mnt/c/Users/shane/Downloads/")
fileToOpen = dataFolder / "dataset_2_7.txt"
with open(fileToOpen) as inFile:
    data = inFile.readlines()

#test = PatternCount(data[0].strip(), data[1].strip())
print(PatternCount("ACTGTACGATGATGTGTGTCAAAG", "TGT"))
print(test)