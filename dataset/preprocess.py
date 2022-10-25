from Bio import SeqIO
import pandas as pd

seq_set : str = set()
seq = []
seq_count = 0

invalid = ['B', 'J', 'O', 'U', 'Z', '*']

with open('gisaid.fasta') as fasta_file:  
    for seq_record in SeqIO.parse(fasta_file, 'fasta'): 
        curr_sequence = str(seq_record.seq)
        if len(curr_sequence) >= 1000:
            check_invalid = False
            for i in invalid:
                if i in curr_sequence:
                    check_invalid = True
                    break
            if curr_sequence not in seq_set and check_invalid is False:
                seq_set.add(curr_sequence)
                seq_count += 1
                print(seq_count)
                
with open('spike-gisaid.txt', 'w') as f:
    for line in seq_set:
        try:
            f.write(line)
            f.write('\n')
        except:
            pass
     
# creating a smaller dataset of 50k sequences   
seq_data = list(seq_set)
seq_data = seq_data[:50000]

with open('spike-gisaid-50k.txt', 'w') as f:
    for line in new_data:
        try:
            f.write(line)
            # f.write('\n')
        except:
            print('err')
            pass

