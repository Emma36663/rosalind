def main():
    import sys
    with open("rosalind_gc.txt", "r") as f:
        lines = f.read().splitlines()  # 按行分割，去掉\n
    
    # 第一步：解析FASTA格式
    dna_records = {}
    current_id = None
    for line in lines:
        if line.startswith('>'):
            current_id = line[1:]  # 去掉>，只存ID
            dna_records[current_id] = ""  # 初始化DNA序列
        else:
            dna_records[current_id] += line  # 拼接DNA
    
    # 第二步：计算GC含量
    def calculate_gc(dna):
        gc = dna.count('G') + dna.count('C')
        total = len(dna)
        return (gc / total) * 100 if total > 0 else 0
    
    # 第三步：找最大值
    max_gc = 0
    max_id = ""
    for dna_id, dna in dna_records.items():
        gc = calculate_gc(dna)
        if gc > max_gc:
            max_gc = gc
            max_id = dna_id
    
    # 第四步：输出结果
    print(f"{max_id}\n{max_gc:.6f}%")

if __name__ == "__main__":
    main()