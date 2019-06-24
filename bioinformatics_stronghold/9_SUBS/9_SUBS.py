with open("input/rosalind_subs.txt") as strings:
    strings = strings.read().strip("\n").split()

locations = ""
location = ""
for i in range(len(strings[0])):
    if (i + len(strings[1]) >= len(strings[0])):
        break
    for j in range(len(strings[1])):
        if strings[0][i+j] == strings[1][j]:
            location = str(i+1) + " "
        else:
            location = ""
            break
    locations += location
locations = locations.strip(" ")

print(locations)
    
output = open("output/loactions.txt", "w") 
output.write(locations) 
output.close()
