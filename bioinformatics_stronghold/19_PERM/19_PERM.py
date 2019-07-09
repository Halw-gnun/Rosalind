with open("input/rosalind_perm.txt") as input_file:
    nr = int(input_file.read().strip("\n"))

def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]
        
def combs(nr):
    seq = []
    for i in range(1, nr+1):
        seq.append(i)
    combinations = []
    for count, combination in enumerate(all_perms(seq)):
        combinations.append(combination)
    return(str(count), combinations)
        
with open("output/variations.txt", "w") as output:
    output.write(combs(nr)[0] + "\n") 
    for comb in combs(nr)[1]:
            output.write(" ".join(map(str, comb)) + "\n") 
            