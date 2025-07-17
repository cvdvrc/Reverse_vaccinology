nextflow.enable.dsl=2

include { CLUSTER }     from './modules/clusterProteins.nf'
include { MHC1 }        from './modules/predictMHC_I.nf'
include { MHC2 }        from './modules/predictMHC_II.nf'
include { BCELL }        from './modules/predictBcell.nf'
include { ANTIGEN }     from './modules/predictAntigenicity.nf'
include { LOCALIZE }    from './modules/predictLocalization.nf'

workflow {

    clustered = CLUSTER(params.input_fasta, params.identity)
    mhc1 = MHC1(clustered.out, params.mhc1_alleles, params.peptide_length)
    mhc2 = MHC2(clustered.out, params.mhc2_alleles)
    bcell = BCELL(clustered.out, params.bcell_method)
    antigenicity = ANTIGEN(mhc1.out)
    localization = LOCALIZE(clustered.out)
}

