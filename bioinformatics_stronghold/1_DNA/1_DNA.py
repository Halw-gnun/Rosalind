myfile = open("input/rosalind_dna.txt")
dna_string = myfile.read().strip("\n")
myfile.close()

count = { "A":0, "C":0, "G":0, "T":0 }
for i in count:
    for j in dna_string:
        if j == i:
            count[i] += 1
            
print(" ".join(list(map(str, count.values()))))

output = open("output/bases.txt", "w") 
output.write(" ".join(list(map(str, count.values())))) 
output.close()