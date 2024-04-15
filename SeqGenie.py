import sys
from fasta_IO import readFasta, getSequencesLength
from FASTA import Fasta


filename=sys.argv[1]

newfasta = Fasta(filename)
newfasta.printFasta()
# print(newfasta.sequences)

# # Read the sequences from the fasta file
# sequences = readFasta(fasta_file)
# # print(sequences)