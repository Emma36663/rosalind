def fasta_to_dna_records(filename):
    dna_records = []
    current_sequence = ""
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace
            if line.startswith('>'):
                # Save previous sequence (if any) and reset
                if current_sequence:
                    dna_records.append(current_sequence)
                    current_sequence = ""
                # Skip the header line
                continue
            else:
                # Append the sequence line (uppercase for consistency)
                current_sequence += line.upper()
        
        # Add the last sequence
        if current_sequence:
            dna_records.append(current_sequence)
    
    return dna_records

# Usage
dna_records = fasta_to_dna_records("rosalind_cons.txt")

string = ["A: ","T: ","C: ","G: "]
ideal = ""

for i in range(len(dna_records[0])): # 先一个位置 不同序号的看
    nucleotide = {'A':0,'T':0,'C':0,'G':0} 
    for nt in dna_records: # 比较是哪一个加一下
        current_nucleotide = nt[i] # 比如说取出dna——records的第一项 让他等于要比较的东西
        nucleotide[current_nucleotide] += 1 #在这里面搜是atcg的那一个那一个得分
    for j,nt in enumerate(['A', 'T','C','G']): # Append count as to string
        string[j] += str(nucleotide[nt]) + ' '
consensus = []
for k in range(len(dna_records[0])):
    counts = {'A':0,'T':0,'C':0,'G':0} 
    for record in dna_records:          # For each sequence
        nt = record[k].upper()          # Ensure uppercase
        counts[nt] += 1 
    max_nt = max(counts, key=counts.get)
    consensus.append(max_nt)
ideal = ''.join(consensus)
print(ideal)
for s in string:
    print(s)