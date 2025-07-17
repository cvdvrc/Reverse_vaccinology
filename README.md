# Bionformatics pipeline for reverse vaccinology

```
nextflow run [pipeline_dir] --input_fasta [clustered_fasta] 
			    --mhc1_alleles [MHC 1 allele]  
			    --mhc2_alleles [MHC2 allelle] 
			    --peptide_length [peptide length] 
			    --identity [cd hit identity] 
			    --bcell_method [Parker, Chou-Fasman, Emini, Karplus-Schulz, Kolaskar-Tongaonkar]
			    -profile [docker]
```
