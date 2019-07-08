with open("input/rosalind_mrna.txt") as input_file:
    seq = [aa for aa in input_file.read().strip("\n")]

#Return possible nr RNA sequences modulo n that may create given peptide sequence
def rna_strings(seq, n=1000000):
    posibilities = 1
    codons = {'A': 4, 'C': 2, 'D': 2, 'E': 2, 'F': 2, 'G': 4, 'H': 2, 'I': 3, 'K': 2, 'L': 6, 'M': 1,
              'N': 2, 'P': 4, 'Q': 2, 'R': 6, 'S': 6, 'T': 4, 'V': 4, 'W': 1, 'Y': 2, '-': 3}
    for aa in seq:
        posibilities *= codons[aa]
    posibilities *= codons["-"]
    return str(posibilities % n)

with open("output/modulo.txt", "w") as output:
    output.write(rna_strings(seq) + "\n") 
        