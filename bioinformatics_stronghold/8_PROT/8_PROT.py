with open("input/RNA_codon_table.txt") as table:
    table = table.read().strip("\n").split()

# Dict of RNA cododns and corresponding protein    
RNA_codon_dict = {}
key = ""
value = ""
for i in range(0, len(table), 2): 
    key = table[i]
    value = table[i+1]
    RNA_codon_dict[key] = value
    
with open("input/rosalind_prot.txt") as RNA_string:
    RNA_string = RNA_string.read().strip("\n")

# Decipher RNA string to protein
protein = ""
for i in range(0, len(RNA_string), 3):
    key = ""
    for j in range(3):
        key += RNA_string[i + j]
    codon = RNA_codon_dict[key]
    
    # Stop the read if Stop is encountered
    if codon != "Stop":
        protein += RNA_codon_dict[key]
    else:
        break
        
print(protein)

output = open("output/protein.txt", "w") 
output.write(protein) 
output.close()
