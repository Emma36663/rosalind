# 导入Biopython的SeqIO模块，用来处理FASTA文件
from Bio import SeqIO

# k: 重叠的碱基数，默认为3
def overlap_graph(fasta_file, k=3):
    # 读取FASTA文件，存储为列表，每个元素是(序列ID, 序列字符串)的元组
    # 例如: [("Rosalind_0498", "AAATAAA"), ("Rosalind_2391", "AAATTTT")]
    sequences = [(record.id, str(record.seq)) for record in SeqIO.parse(fasta_file, "fasta")]
    
    # 初始化一个空列表，用来存储结果边（例如 ["ID1 ID2", "ID2 ID3"]）
    edges = []
    
    # 双重循环：比较所有可能的序列对 (s, t)
    for s_id, s_seq in sequences:      # s是当前序列
        for t_id, t_seq in sequences:  # t是目标序列
            # 条件1: 禁止自环（s和t不能是同一个序列）
            # 条件2: s的最后k个碱基 == t的前k个碱基
            if s_id != t_id and s_seq[-k:] == t_seq[:k]:
                # 如果满足条件，将这对ID加入edges列表（格式："ID1 ID2"）
                edges.append(f"{s_id} {t_id}")
    return edges

fasta_file = "/Users/emmajiang/Desktop/rosalind folder/stronghold/rosalind_grph.txt"

edges = overlap_graph(fasta_file)

# 打印结果：每条边占一行
print("\n".join(edges))