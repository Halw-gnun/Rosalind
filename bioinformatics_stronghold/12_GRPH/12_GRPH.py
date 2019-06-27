input_file = open("input/rosalind_grph.txt", "r")

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

output = []
for key, value in fasta.items():
    for keys, values, in fasta.items():
        if value[-3:] == values[0:3] and value != values:
            output.append([key, keys])        
            
adjacency_list = ('\n'.join([' '.join(['{:1}'.format(graph) for graph in edge]) for edge in output])+"\n")

print(adjacency_list)

output = open("output/adjacency.txt", "w") 
output.write(adjacency_list) 
output.close()
