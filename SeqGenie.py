import sys
from FASTA import Fasta


print("This is Program Name:", sys.argv[0])

filename=sys.argv[1]
newfasta = Fasta(filename)
# newfasta.printFasta()

# Next should return FASTA

Leuconostoc = newfasta.searchHeader("Leuconostoc")
print(type(Leuconostoc))