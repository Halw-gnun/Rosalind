input_file = open("input/rosalind_rna.txt", "r")
dna_string = input_file.read().strip("\n")
input_file.close()

rna_string = ""

for i in dna_string:
    if i == "T":
        rna_string += "U"
    else:
        rna_string += i
        
print(rna_string)

output = open("output/RNA.txt", "w") 
output.write(rna_string) 
output.close() 