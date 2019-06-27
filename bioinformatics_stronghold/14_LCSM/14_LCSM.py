input_file = open("input/rosalind_lcsm.txt", "r")

fasta_dict = {}
name = ''

#Create dict from fasta.text with name of DNA string as index, and string composition as value
for line in input_file:
    if line.startswith('>'):
        name = line[1:-1]
        fasta_dict[name] = ""
    else:
        fasta_dict[name] += line.strip()
input_file.close()


#Return the first detected longest common substring
def longest_common(fasta_dict):
    seqs = fasta_dict.values()
    shortest = min(seqs)
    for i in range(len(shortest)):
        lenght = len(shortest)-i
        for start in range(len(shortest)):
            stop = start+lenght
            if stop > len(shortest):
                break
            sub = shortest[start:stop]
            if all(seq.find(sub) >= 0  for seq in seqs):
                return(sub)    

substring = longest_common(fasta_dict) + "\n"
print(substring)

output = open("output/substring.txt", "w") 
output.write(substring) 
output.close()
