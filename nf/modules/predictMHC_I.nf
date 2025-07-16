process MHC1 {

    tag "$input_fasta"

    input:
    path input_fasta
    val allele_file
    val peptide_length
    

    output:
    path "mhc1_predictions.tsv", emit: out

    script:
    """
    python3 /usr/bin/predict_binding ann $allele_file $peptide_length $input_fasta > mhc1_predictions.tsv
    """
}

