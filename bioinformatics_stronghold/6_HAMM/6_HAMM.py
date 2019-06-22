input_file = open("input/rosalind_hamm.txt", "r")
strands = input_file.read().strip("\n").split()
input_file.close()

miss = 0

for i in range(len(strands[0])):
    if strands[0][i] != strands[1][i]:
        miss += 1

print(miss)

output = open("output/miss.txt", "w") 
output.write(str(miss)) 
output.close() 
