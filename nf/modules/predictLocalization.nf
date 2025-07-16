process LOCALIZE {

    tag "$fasta"

    input:
    path fasta

    output:
    path "localization_results.tsv", emit: out

    script:
    """
    phobius -short $fasta > localization_results.tsv
    """
}

