## Bionformatics pipeline for reverse vaccinology
# Download sequences: 
> get_sequences. py

# Clusterisation: 
> cd-hit -i proteomes_ncbi.fasta -o cd_hit_proteome_clustered.fasta -c 0.90 -n 5

# Predictions
> python3 IApred.py cd_hit_proteome_clustered.fasta
