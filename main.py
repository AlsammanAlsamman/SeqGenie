

SeqDict = {
    "seq1": "ATCGATCGATCGATCGATCGATCGATCGATCG",
    "seq2": "ATCGATCGATCGATCGATCGATCGATCGATCG",
    "seq3": "ATCGATCGATCGATCGATCGATCGATCGATCG"
}



def getSeqLength(SeqDict):
    seqLength =  {}
    print(seqLength)
    for key in SeqDict:
        print(key)
        seqLength[key] = len(SeqDict[key])
        print(len(SeqDict[key]))
        print(seqLength)
    return seqLength

# Must be called from main.py
print(getSeqLength(SeqDict))
