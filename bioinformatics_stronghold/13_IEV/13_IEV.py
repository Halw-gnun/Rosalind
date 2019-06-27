input_file = open("input/rosalind_iev.txt", "r")
couples = [int(x) for x in input_file.read().strip("\n").split(" ")]
input_file.close()

def expected_offspring(couples, offspring=2):
    
    probability = [1, 1, 1, 0.75, 0.5, 0]
    expected_offspring = 0
    for i in range(len(couples)):
        expected_offspring += couples[i] * probability[i] * offspring
    return expected_offspring

expected = expected_offspring(couples)
print(expected, "\n")

output = open("output/expected.txt", "w") 
output.write(str(expected) + "\n") 
output.close() 
