input_file = open("input/rosalind_fibd.txt", "r")
n, m = input_file.read().strip("\n").split(" ")
input_file.close()

def fib(n, m, k=1):
    dead = [0]*m + [1]
    pairs = [1, 1]
    previous1, previous2 = 1, 1
    for i in range(2, n):
        dead.append(k*(previous2))
        current = previous1 + k * previous2 - dead[i]
        previous2 = previous1
        previous1 = current
        pairs.append(current)
    return pairs[n-1]

rabbit_pairs = fib(int(n), int(m))
print(rabbit_pairs)

output = open("output/rabbit_pairs.txt", "w") 
output.write(str(rabbit_pairs)) 
output.close() 
