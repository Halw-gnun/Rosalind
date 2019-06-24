input_file = open("input/rosalind_cons.txt", "r")

fasta = {}
name = ''

#Create dict from fasta.text with name of DNA string as index, and string composition as value
for line in input_file:
    if line.startswith('>'):
        name = line[1:-1]
        fasta[name] = ""
    else:
        fasta[name] += line.strip()
input_file.close()

# Find length of longest inserted string
length = 0
for value in fasta.values():
    if length < len(value):
        length = len(value)

# Freq of nucleotides at spec position
profile = {"A": [0] * length, "C": [0] * length, "G": [0] * length, "T": [0] * length}
for value in fasta.values():
    count = 0
    for nucleotide in value:
        for key in profile.keys():
            if nucleotide == key:
                profile[key][count] += 1
                break
        count += 1

# Find most frequent nucleotide for all positions
consensus = ""
for pos in range(length):
    temp_value = 0
    for key, value in profile.items():
        if temp_value < value[pos]:
            temp_value = value[pos]
            temp_key = key
    consensus += temp_key
        
print(consensus + '\n' + '\n'.join([key + ":" + ''.join(['{:2}'.format(item) for item in value]) for key, value in profile.items()]))

output = open("output/consensus.txt", "w") 
output.write(consensus + '\n' + '\n'.join([key + ":" + ''.join(['{:2}'.format(item) for item in value]) for key, value in profile.items()])) 
output.close() 
