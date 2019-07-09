input_file = open("input/rosalind_orf.txt", "r")

dna_dict = {}
name = ''

#Create dict from fasta.text with name of DNA string as index, and string composition as value
for line in input_file:
    if line.startswith('>'):
        name = line[1:-1]
        dna_dict[name] = ""
    else:
        dna_dict[name] += line.strip()
input_file.close()

#Return complementary RNA seq for all given DNA seq in a dict
def transcription(dna_dict):
    for key, dna in dna_dict.items():
        rna_dict[key] = dna.upper().replace("T", "U")
    return rna_dict

#Returns start possition of all possible ORFs from given DNA seq
def orf(dna_dict):
    rna_dict = transcription(dna_dict)
    for rna_seq in rna_dict.values():
        pos = 0
        starts = []
        while True:
            start = rna_seq.find("AUG", pos)
            if start != -1:
                starts.append(start)
                pos = start+1
            else:
                pos = 0
                break 
    return (starts, rna_seq)
                
#Returns protein seq for every given start possition            
def translation(dna_dict):
    (starts, rna_seq) = orf(dna_dict)
    proteins =[]
    for start in starts:
        protein_seq = []
        for i in range(start, len(rna_seq), 3):
            codon = (rna_seq[i:i+3])
            if translate_codon(codon)== "-":
                proteins.append(protein_seq)
                break
            else:
                protein_seq.append(translate_codon(codon))
    return proteins

#Returns aa for every given codon
def translate_codon(codon):
    decipher = { "UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
                 "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
                 "UAU":"Y", "UAC":"Y", "UAA":"-", "UAG":"-",
                 "UGU":"C", "UGC":"C", "UGA":"-", "UGG":"W",
                 "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
                 "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
                 "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
                 "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
                 "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
                 "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
                 "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
                 "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
                 "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
                 "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
                 "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
                 "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}
    for key, aa in decipher.items():
        if key == codon:
            return aa
        
#Returns dict of reverse strands for given dict of DNA strands
def reverse_complement(dna_dict):
    reverse_dict = {}
    rev = ""
    swap  = {"A":"T", "T":"A", "G":"C", "C":"G"}
    for key, dna in dna_dict.items():
        for nuc in dna.upper():
            for current, new in swap.items():
                if current == nuc:
                    rev += new
        reverse_dict[key] = rev[::-1]
    return reverse_dict

def posibilites(dna_dict):
    reverse = reverse_complement(dna_dict)
    proteins_rev = translation(reverse)
    proteins_fw = translation(dna_dict)
    for fw in proteins_fw:
        if fw not in proteins_rev: 
            proteins_rev.append(fw)
    return proteins_rev

posibilites(dna_dict)

with open("output/protein.txt", "w") as output:
    for seq in posibilites(dna_dict):
        output.write("".join(seq) + "\n") 
        