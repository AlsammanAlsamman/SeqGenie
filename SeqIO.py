import os
import sys

# Read a fasta file and return a dictionary with the sequences
# file: the fasta file name and path
# return: a dictionary with the sequences {seqid: {'info': 'header info', 'seq': 'sequence'}, ...}
def readFasta(file):
    # >seq1 [species] [gene] [other]
    # ATCGATCGATCG
    sequences = {}
    with open(file, 'r') as f:
        for line in f:
            if line == '\n':
                continue
            if line.startswith('>'):
                # To remove ">" and split the header into a list using the space
                header = line[1:].strip().split() # became a list
                seqid = header[0] # The first value in the list (seq ID)
                info=" ".join(header[1:])
                sequences[seqid] = {'info':info, 'seq':''}
            else:
                sequences[seqid]['seq'] += line.strip()
    return sequences


def writeFasta(sequences, outfile, singline=False,blocksize=60, tensblock=False):
    with open(outfile, 'w') as f:
        for seqid, seqinfo in sequences.items():
            f.write('>' + seqid + ' ' + seqinfo['info'] + '\n')
            if singline:
                f.write(seqinfo['seq'] + '\n')
            else:
                for i in range(0, len(seqinfo['seq']), blocksize):
                    current_block = seqinfo['seq'][i:i+blocksize]
                    # split to 10s blocks
                    if tensblock:
                        for j in range(0, len(current_block), 10):
                            f.write(current_block[j:j+10] + ' ')
                    else:
                        f.write(current_block)
                f.write('\n')

def create_seq(seqid, seqinfo, seq):
    if seqid != None and seqinfo != None and seq != None:
        return {seqid: {'info': seqinfo, 'seq': seq}}
    else:
        # throw an error and return na
        print('Error: seqid, seqinfo and seq must be provided', __name__, sys._getframe().f_code.co_name)
        exit(1)

if __name__ == '__main__':
    filename = sys.argv[1]
    sequences = readFasta(filename)
    oufile = filename.split('.')[0] + '_new.fasta'
    writeFasta(sequences, oufile, blocksize=60, tensblock=True)