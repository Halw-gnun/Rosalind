input_file = open("input/rosalind_fib.txt", "r")
nk = input_file.read().strip("\n").split(" ")
input_file.close()

info = { "months": int(nk[0]), "litter_pairs": int(nk[1])}
rabbit_pairs = {}


for i in range(1, info["months"]+1):
    if i-2 >= 1:
        rabbit_pairs[i] = rabbit_pairs[i-1] + info["litter_pairs"]*rabbit_pairs[i-2]
    else:
        rabbit_pairs[i] = 1
        
print(rabbit_pairs)
print(rabbit_pairs[info["months"]])

output = open("output/rabbit_pairs.txt", "w") 
output.write(str(rabbit_pairs[info["months"]])) 
output.close() 
