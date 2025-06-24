#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Aminata NDIAYE
# CVD - VCR - IPD
# 06/2025
# Tested with python3
# Version 1.0.0
# Usage: python3 get_sequences.py -q "rift virus[Organism] AND complete genome" -d nucleotide -rt fasta -rm text -rmx 10000 -o viral_protein.fasta

import argparse
from Bio import Entrez, SeqIO

parser = argparse.ArgumentParser(description="Download genomic or proteic sequences into one single fasta file using Biopython toolkit.")
parser.add_argument("-q", "--query",help="Query entered for searching.")
parser.add_argument("-d", "--database",help="Database in which to search.")
parser.add_argument("-rt", "--rettype", help="Output file rettype.", default="fasta")
parser.add_argument("-rm", "--retmode", help="Output file retmode.", default="text")
parser.add_argument("-rmx", "--retmax", help="Output file retmax.", default="10000")
parser.add_argument("-o", "--output", help="Output file")
args = parser.parse_args()

print(f"Query: {args.query}")
print(f"Database: {args.database}")
print(f"Retype: {args.rettype}")
print(f"Retmode: {args.retmode}")
print(f"Output: {args.retmax}")
print(f"Output: {args.output}")


Entrez.email = "cvd-vrc@pasteur.sn"
#query = "measles virus[Organism] AND complete genome"

handle = Entrez.esearch(db=args.database, term=args.query, retmax=args.retmax)
record = Entrez.read(handle)
ids = record["IdList"]

with open(args.output, "w") as out_handle:
    for start in range(0, len(ids), 100):
        end = min(len(ids), start + 100)
        fetch_ids = ids[start:end]
        handle = Entrez.efetch(db=args.database, id=fetch_ids, rettype=args.rettype, retmode=args.retmode)
        sequences = handle.read()
        out_handle.write(sequences)
