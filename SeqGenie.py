
#!/usr/bin/env python3

fasta_file = "sampledata/sequences.fasta"

# Read the fasta file
sequences = {} # empty dictionary
seqid = "" # FN356739.1 (currrent value)
sequence = "" #"ACGGGTGAGTAACACGTGGGCAACCTGCCTCAGAGTGGGGGATAACACCGGGAAATCGGTGCTAATACCG" (current value)

with open(fasta_file, "r") as f_data:
    for line in f_data:
        # line  = ">FN356739.1 [gene=16S rRNA] [location=<1..969] [gbkey=Gene]\n"
        # line = ">FN356739.1 [gene=16S rRNA] [location=<1..969] [gbkey=Gene]"
        # seqheader = "FN356739.1 [gene=16S rRNA] [location=<1..969] [gbkey=Gene]"
        # header_list = ["FN356739.1", "[gene=16S","rRNA]", "[location=<1..969]", "[gbkey=Gene]"]
        # seqid = "FN356739.1"
        if line.startswith(">"):
            # header
            line = line.strip()
            seqheader = line[1:]
            header_list = seqheader.split(" ")
            seqid = header_list[0]
            sequences[seqid] = "" # value intialization of string type
        else:
            # sequence
            line = line.strip() # remove the newline character
            sequence = line
            sequences[seqid] = sequences[seqid] + sequence
            # new value of key seqid = old value of key seqid + new value of sequence
            # sequences[seqid] += sequence also works


######################## Modify ############################

fasta_file = "sampledata/sequences.fasta"

# Read the fasta file
sequences = {} # empty dictionary
seqid = "" # FN356739.1 (currrent value)
sequence = "" #"ACGGGTGAGTAACACGTGGGCAACCTGCCTCAGAGTGGGGGATAACACCGGGAAATCGGTGCTAATACCG" (current value)


with open(fasta_file, "r") as f_data:
    for line in f_data:
        # line  = ">FN356739.1 [gene=16S rRNA] [location=<1..969] [gbkey=Gene]\n"
        # line = ">FN356739.1 [gene=16S rRNA] [location=<1..969] [gbkey=Gene]"
        # seqheader = "FN356739.1 [gene=16S rRNA] [location=<1..969] [gbkey=Gene]"
        # header_list = ["FN356739.1", "[gene=16S","rRNA]", "[location=<1..969]", "[gbkey=Gene]"]
        # seqid = "FN356739.1"
        if line.startswith(">"):
            # header
            line = line.strip()
            seqheader = line[1:]
            header_list = seqheader.split(" ")
            seqid = header_list[0]
            sequences[seqid] = {"header": seqheader, "sequence": ""}
        else:
            # sequence
            line = line.strip() # remove the newline character
            sequence = line
            sequences[seqid]["sequence"] = sequences[seqid]["sequence"] + sequence
        

# Print the sequences
for seqid in sequences.keys():
    print("Sequence ID:", seqid)
    print("Header:", sequences[seqid]["header"])
    print("Sequence:", sequences[seqid]["sequence"])