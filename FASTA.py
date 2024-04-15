from fasta_IO import *

class Fasta:
    def __init__(self, fastapath):
        self.filepath = fastapath
        self.sequences = readFasta(fastapath)

    def printFasta(self):
        print("This is the fasta file: ", self.filepath)
        sequences = self.sequences
        sequenceLength = getSequencesLength(sequences)
        for seqid in sequences:
            print("Sequence ID: ", seqid)
            print("Header: ", sequences[seqid]["header"])
            print("Sequence Length: ", sequenceLength[seqid])
            # print("Sequence: ", sequences[seqid]["sequence"])
            print("\n")

    def searchHeader(self, pattern):
        subSequences = searchHeader(self.sequences, pattern)
        return subSequences