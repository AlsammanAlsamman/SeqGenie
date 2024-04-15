from fasta_IO import readFasta, getSequencesLength

class Fasta:
    def __init__(self, fastapath):
        self.filepath = fastapath
        self.sequences = readFasta(fastapath)

    def printFasta(self):
        print("This is the fasta file: ", self.filepath)
        sequences = self.sequences
        for seqid in sequences:
            print("Sequence ID: ", seqid)
            print("Header: ", sequences[seqid]["header"])
            print("Sequence: ", sequences[seqid]["sequence"])
            print("\n")