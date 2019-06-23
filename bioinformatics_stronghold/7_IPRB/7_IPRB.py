# Put values in dict with corresponding name key
with open("input/rosalind_iprb.txt") as input_file:
    (gene_type["dom"], gene_type["het"], gene_type["rec"]) = input_file.read().strip("\n").split()

# Turn str values into int
# Checks total amount of animals
total = 0
for key, value in gene_type.items():
    gene_type[key] = float(value)
    total += float(value)

# Probability for first pick of animal
first_pick = {}
for key, value in gene_type.items():
    first_pick[key] = value/total

# Probability for combinations of first and second pick
second_pick = {}
sec_prob = 0
for key, value in gene_type.items():
    for key_first, value_first in first_pick.items():
        if key == key_first:
            sec_prob = (value-1)/(total-1)
        else:
            sec_prob = (value)/(total-1)
        second_pick[key + " " + key_first] = sec_prob*value_first

# Sum of probability for picks resulting in at least one dominant allele
prob_sum = 0
for key, value in second_pick.items():
    # Picks with 100% chance of resulting in at least one dominant allele
    if "dom" in key.lower():
        prob_sum += value
    # Picks with 75% chance of resulting in one dominant allele
    if "het het" in key.lower():
        prob_sum += value*0.75
    # Picks with 50% chance of resulting in one dominant allele
    if key == "rec het" or key == "het rec":
        prob_sum += value/2
    
print(prob_sum)

output = open("output/probability.txt", "w") 
output.write(str(prob_sum)) 
output.close()
