with open("/Users/emmajiang/Desktop/rosalind folder/stronghold/rosalind_iev.txt", 'r') as f:
   num = list(map(int,f.read().split()))

prob = [1.0,1.0,1.0,0.75,0.5,0.0]
total = 0

for i in range(6):
    current = num[i]*2*prob[i]
    total += current

print(total)