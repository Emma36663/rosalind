with open("rosalind_dna.txt",'r')as f:
    content = f.read()
print(content)
count_A = content.count('A')
print(count_A)
count_C = content.count('C')
print(count_C)
count_G = content.count('G')
print(count_G)
count_T = content.count('T')
print(count_T)