with open("rosalind_revc.txt","r")as f:
    content = f.read()
content = content[::-1]
print(content)

nlen = len(content)
for i in range(nlen):
    ch = content[i]
    if ch == 'A':
        ch = 'T'
    elif ch == 'T':
        ch = 'A'
    elif ch == 'G':
        ch = 'C'
    elif ch == 'C':
        ch = 'G'
    content = content[:i] + ch + content[i+1:]
print(content)