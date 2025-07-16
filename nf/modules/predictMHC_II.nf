process MHC2 {

    tag "$input_fasta"

    input:
    path input_fasta
    val allele_file

    output:
    path "mhc2_predictions.tsv", emit: out

    script:
    """
    python /usr/bin/mhc_II_binding netmhciipan_el $allele_file $input_fasta > mhc2_predictions.tsv
    """
}

