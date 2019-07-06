with open("input/rosalind_lia.txt") as input_file:
    generations, organisms = input_file.read().strip("\n").split()
    
#Calculates the total progeny of one generation
def population(generations, progeny=2):
    generation_population = progeny ** generations
    return(generation_population)

#Calculates the Distribution of different possible genotypes of progeny
#where one parent is AaBb and the second of your own choice
def mendels_second_law(dad, mom="AaBb"):
    egg = []
    sperm = []
    genotypes = []
    genotype = []
    sum_genotypes = {}
    for i in mom[0:2]:
        for j in dad[2:4]:
            egg.append(i + j)
    for i in dad[0:2]:
        for j in mom[2:4]:
            sperm.append(i + j)
    for e in egg:
        for s in sperm:
            genotype = "".join(sorted(e[0] + s[0]) + sorted(e[1] +s[1]))
            genotypes.append(genotype)  
    for gene in genotypes:
        if gene in sum_genotypes.keys():
            sum_genotypes[gene] += 1
        else: 
            sum_genotypes[gene] = 1          
    return sum_genotypes

#Calculates the Probability of different possible genotypes of progeny
#where one parent is AaBb and the second of your own choice
def genotype_probs(parent2):
    sum_genotypes = mendels_second_law(parent2)
    values = 0
    probabilities = {}
    for value in sum_genotypes.values():
        values += value
    for key,value in sum_genotypes.items():
        probabilities[key] = sum_genotypes[key]/values
    return probabilities

#Calculate probability of different genotypes following several generations
def generation_probs(generations):
    probs_dict = genotype_probs("AaBb")
    #Calculate the probability of different genotypes for each generation
    for generation in range(generations):
        new_probs_dict = {}
        for key, value in probs_dict.items(): 
            key_probs_dict = genotype_probs(key)
            for key_key, key_value in key_probs_dict.items():
                if key_key in new_probs_dict.keys():
                    new_probs_dict[key_key] += value*key_value
                else:
                    new_probs_dict[key_key] = value*key_value
        probs_dict = new_probs_dict         
    return new_probs_dict

#Calculates the factorial of inserted value(n)
def factorial(n):
    prod = 1
    for k in range(2,n+1):
        prod *= k
    return prod
    
#Probability for at least amount of organisms(k) with genotype AaBb in population(n) of a certain generation
def cumulative_distribution(k, generations):
    k = int(k)
    n = population(int(generations))
    p = generation_probs(int(generations))["AaBb"] #Would be fine to make it 0.25 and
    prob = 0
    for i in range(k):
        prob += (factorial(n)/(factorial(i)*factorial(n-i)))*(p**i)*((1-p)**(n-i))
    return(1-prob)
        
prob = cumulative_distribution(organisms, generations)
print(prob)

output = open("output/probability.txt", "w") 
output.write(str(prob) + "\n") 
output.close() 
