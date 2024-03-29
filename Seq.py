from SeqIO import readFasta, writeFasta, create_seq
import sys

class Seq:
    def __init__(self, filename=None, seqID=None, seqInfo=None, seq=None):
        if filename:
            self.filename = filename
            self.sequences = readFasta(filename)
        else:
            self.sequences = create_seq(seqID, seqInfo, seq)
            self.filename = None

        if not self.sequences:
            print('Error: sequences must be provided', __name__, sys._getframe().f_code.co_name)
            exit(1)


if __name__ == '__main__':
    filename = sys.argv[1]
    seq = Seq( seqInfo='[species] [gene] [other]', seq='ATCGATCGATCG')
    # seq = Seq(filename)
    print(seq.filename)
    print(seq.sequences)

#     # oufile = filename.split('.')[0] + '_new.fasta'
#     # writeFasta(seq.sequences, oufile, blocksize=60, tensblock=True)
