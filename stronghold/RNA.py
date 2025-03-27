with open("rosalind_rna.txt", "r")as f:
    content = f.read()

new_content = content.replace("T","U")
print(new_content)