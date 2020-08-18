import random as rd

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

def hammDist(seq1, seq2, d=-1):
    dist = 0
    if len(seq1) != len(seq2):
        return -1
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            dist += 1
        if d != -1 and dist > d:
            return -1
    return dist

def profileMost(Text, k, Profile):
    profMax = 0.0
    kmerMax = Text[:k]
    for i in range(len(Text) - k + 1):
        kmer = Text[i:i+k]
        tProf = 1.0
        for x in range(k):
            tProf *= Profile[symToNum(kmer[x])][x]
        if tProf > profMax:
            profMax = tProf
            kmerMax = kmer
    return kmerMax

def makeProfile(Dna, pCounts=True):
    prof = [[0] * len(Dna[0]) for _ in range(4)]
    for string in Dna:
        for i in range(len(string)):
            prof[symToNum(string[i])][i] += 1
    if pCounts:
        return [[(x+1)/(len(Dna) + 4) for x in i] for i in prof]
    else:
        return [[x/len(Dna) for x in i] for i in prof]

def makeCon(prof):
    con = ''
    test = list(zip(*prof))
    for pos in test:
        con += numToSym(pos.index(max(pos)))
    return con

def score(motifs, pCounts=True):
    prof = makeProfile(motifs, pCounts)
    con = makeCon(prof)
    score = [hammDist(con, x) for x in motifs]
    return sum(score)

def randMotif(Dna, k):
    rd.seed()
    ran = rd.randint(0,len(Dna[0]) - k + 1)
    res = []
    for seq in Dna:
        res.append(seq[ran:ran+k])
    return res

def mostProb(tProf, Dna, k):
    newMotif = []
    for seq in Dna:
        newMotif.append(profileMost(seq, k, tProf))
    return newMotif

def randMotifSearch(Dna, k, t, pCounts=True):
    bestMotifs = randMotif(Dna, k)
    bestScore = score(bestMotifs)
    for i in range(1000):
        if i == 0:
            tMotifs = bestMotifs
        else:
            tMotifs = randMotif(Dna, k)
        rMotifs = tMotifs
        rScore = score(tMotifs)
        while True:
            tProf = makeProfile(tMotifs)
            tMotifs = mostProb(tProf, Dna, k)
            tScore = score(tMotifs)
            if tScore < rScore:
                rScore = tScore
                rMotifs = tMotifs
            else:
                break
        if rScore < bestScore:
            bestMotifs = rMotifs
            bestScore = rScore
    return bestMotifs
        
dna = ['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA', 'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG', 'TAGTACCGAGACCGAAAGAAGTATACAGGCGT', 'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC', 'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']
randMotifSearch(dna, 8, 5)