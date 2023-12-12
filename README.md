# GenoTools

## Getting Started

GenoTools is a suite of automated genotype data processing steps written in Python. The core pipeline was built for Quality Control and Ancestry estimation of data in the Global Parkinson's Genetics Program (GP2)

you can pull the most current references by running:
```
genotools-download
```
By default, the reference panel will be downloaded to ~/.genotools/ref. but can be download to a location of choice with `--destination`.

To download specific references/models, you can run the download with the following options:
```
genotools-download --ref 1kg_30x_hgdp_ashk_ref_panel --model nba_v1 --destination /path/to/download_directory/
```

Currently, `1kg_30x_hgdp_ashk_ref_panel` is the only available reference panel. Available models are `nba_v1` for the NeuroBooster array and `neurochip_v1` for the NeuroChip Array. If using a different array, we would suggest training a new model by running the standard command below.

Modify the paths in the following command to run the standard GP2 pipeline:
```
genotools \
  --pfile /path/to/genotypes/for/qc \
  --out /path/to/qc/output \
  --ancestry \
  --ref_panel /path/to/reference/panel \
  --ref_labels /path/to/reference/ancestry/labels \
  --all_sample \
  --all_variant
```

if you'd like to run the pipeline using an existing model, you can do that like so (take note of the `--model` option):
```
genotools \
  --pfile /path/to/genotypes/for/qc \
  --out /path/to/qc/output \
  --ancestry \
  --ref_panel /path/to/reference/panel \
  --ref_labels /path/to/reference/ancestry/labels \
  --container \
  --all_sample \
  --all_variant
  --model nba_v1
```

if you'd like to run the pipeline using the default nba_v1 model in a Docker container, you can do that like so:
```
genotools \
  --pfile /path/to/genotypes/for/qc \
  --out /path/to/qc/output \
  --ancestry \
  --ref_panel /path/to/reference/panel \
  --ref_labels /path/to/reference/ancestry/labels \
  --container \
  --all_sample \
  --all_variant
  --model nba_v1
```
Note: add the ```--singularity``` flag to run containerized ancestry predictions on HPC

This will find common snps between your genotype data and the reference panel, run PCA, UMAP-transform PCs, and train a new XGBoost classifier specific to your data/ref panel.

genotools accept `--pfile`, `--bfile`, or `--vcf`. Any bfile or vcf will be converted to a pfile before running any steps. 

## Documentation
- [GenoTools Command Line Arguments](https://github.com/dvitale199/GenoTools/blob/main/docs/cli_args.md)
- [Default Pipeline Overview](https://github.com/dvitale199/GenoTools/blob/main/docs/default_pipeline_overview.md)
- [Package Function Guide (for developers)](https://github.com/dvitale199/GenoTools/blob/main/docs/genotools_function_guide.md)

## Acknowledgements
GenoTools was developed as the core genotype and wgs processing pipeline for the Global Parkinson's Genetics Program (GP2) at the Center for Alzheimer's and Related Dementias (CARD) at the National Institutes of Health.

This tool relies on PLINK, a whole genome association analysis toolset, for various genetic data processing functionalities. We gratefully acknowledge the developers of PLINK for their foundational contributions to the field of genetics. More about PLINK can be found at [their website](https://www.cog-genomics.org/plink/2.0/).



