with open("rosalind_hamm.txt", 'r') as f:
    lines = f.read().splitlines()

dna_strip_1 = lines[0]
print(dna_strip_1)
dna_strip_2 = lines[1]
distance = 0

for check in range(len(dna_strip_1)):
    if dna_strip_1[check] != dna_strip_2[check]:
        distance += 1

print(distance)