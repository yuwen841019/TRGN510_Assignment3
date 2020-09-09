from gtfparse import read_gtf
import sys
import json

df = read_gtf(sys.argv[1])

gene_df = df[['gene_name', 'seqname', 'start', 'end']]
gene_df.columns = ['geneName', 'chr', 'startPos', 'endPos']

gtf2json = gene_df.to_json(orient="records",force_ascii=False)

with open('Homo_sapiens.GRCh37.75.json', 'w') as f1:
    json.dump(gtf2json, f1)                
