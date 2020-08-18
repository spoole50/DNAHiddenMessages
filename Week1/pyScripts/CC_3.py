from pathlib import Path

#Generate Reverse Compliment of a given DNA seq
def reverseComp(seq):
    res = ""
    codon = {'A': 'T',
             'T': 'A',
             'G': 'C',
             'C': 'G'}
    for i in range(len(seq) - 1, -1, -1):
        res += codon[seq[i]]
    print(res)

#reverseComp("AAAACCCGGT")

dataFolder = Path("/mnt/c/Users/shane/Downloads/")
fileToOpen = dataFolder / "dataset_3_2.txt"
with open(fileToOpen) as inFile:
    data = inFile.readlines()

reverseComp(data[0].strip())