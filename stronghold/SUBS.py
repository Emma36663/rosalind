with open('rosalind_subs.txt','r')as f:
    s, t = f.read().splitlines()

for i in range(1,len(s)-len(t)+1):
    if t == s[i-1:i+len(t)-1]:
        print(i, end= ' ')