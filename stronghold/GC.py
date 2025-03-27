with open("rosalind_gc.txt","r") as f:
    lines = f.read().splitlines()

dna_records = {}
current_id = None

for line in lines:
    line = line.strip() # 去掉空格和换行
    if line.startswith('>'):
        current_id = line[1:]
        dna_records[current_id] = ""
    else: 
        dna_records[current_id] += line
    
def calculate_gc(dna):
    gc = dna.count('G') + dna.count('C')
    total = len(dna)
    divide = (gc/total) * 100 if total > 0 else 0
    return divide

max_gc = 0
max_id = ""
for dna_id, dna in dna_records.items():
    gc = calculate_gc(dna)
    if gc > max_gc:
        max_gc = gc
        max_id = dna_id

print(f'{max_id}\n{max_gc}')

