process BCELL {

    tag "$input_fasta"

    input:
    path input_fasta
    val bcell_method
    

    output:
    path "bcell_predictions.tsv", emit: out

    script:
    """
    python /usr/bin/predict_antibody_epitope -m $bcell_method -f $input_fasta > bcell_predictions.tsv
    """
}

