input_file = open("input/rosalind_gc.txt", "r")

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

content = {}
key = ""
highest = 0

#Check all submitted DNA strings
for string in fasta:
    GC = 0.
    total = 0.
    
    #Check GC content for current DNA string
    for nucleotide in fasta[string]:
        if nucleotide in ["G", "C"]:
            GC += 1.
            total += 1.
        else:
            total += 1.
    content[string] = GC/total*100
    
    #Check if current DNA string has the highest GC content
    if content[string] > highest:
        highest = content[string]
        key = string

print(content)
print(key)
print(content[key])

output = open("output/highest_GC.txt", "w") 
output.write(key + "\n" + str(content[key])) 
output.close() 