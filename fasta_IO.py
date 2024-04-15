def readFasta(fasta_file):
    sequences = {} # empty dictionary 
    seqid = "" # FN356739.1 (currrent value)
    with open(fasta_file, "r") as f_data:
        for line in f_data:
            if ">" in line:
                seqheader = line.strip()
                seqheader = seqheader[1:]
                seqid = seqheader.split()[0]
                sequences[seqid] = {"header": seqheader, "sequence": ""}
            else:
                # This is a sequence line
                sequence = line.strip()
                sequences[seqid]["sequence"] += sequence
    return sequences

def getSequencesLength(sequences):
    seqLength = {}
    for seqid in sequences:
        seqLength[seqid] = len(sequences[seqid]["sequence"])
    return seqLength
