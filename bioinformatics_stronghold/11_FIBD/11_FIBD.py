input_file = open("input/rosalind_fibd.txt", "r")
nm = input_file.read().strip("\n").split(" ")
input_file.close()

info = { "months": int(nm[0]), "life_span": int(nm[1]), "litter_pairs": 1}
rabbit_pairs = {}


dying = [0]
old = 0
present = 0
for i in range(1, info["months"]+1):
    if i > info["life_span"]+1:
        old = rabbit_pairs[i-(info["life_span"]+1)]
        
    if i > info["life_span"]:
        present = rabbit_pairs[i-(info["life_span"])]
    dying.append(present - old)
    if i-2 >= 1:
        rabbit_pairs[i] = rabbit_pairs[i-1] + info["litter_pairs"]*(rabbit_pairs[i-2]-dying[i-1]) - dying[i]
    else:
        rabbit_pairs[i] = 1

print(rabbit_pairs[info["months"]])

output = open("output/rabbit_pairs.txt", "w") 
output.write(str(rabbit_pairs[info["months"]])) 
output.close()
