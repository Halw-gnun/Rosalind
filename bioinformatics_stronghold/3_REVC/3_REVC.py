input_file = open("input/rosalind_revc.txt", "r")
dna_string = input_file.read().strip("\n")
input_file.close()

comp_template = { "A":"T", "C":"G", "G":"C", "T":"A" }
reverse_complement = ""

for i in reversed(dna_string):
    for j in comp_template:
        if i == j:
            reverse_complement += comp_template[j]

print(reverse_complement)

output = open("output/reverse_complement.txt", "w") 
output.write(reverse_complement) 
output.close() 
