# Bac2Feature macOS Setup Notes

## Local Python environment (uv)
- `uv venv` then `source .venv/bin/activate`.
- Install this repo in editable mode with packaged data: `uv pip install -e .` or `uv pip install --force-reinstall .`
- Homebrew BLAST+ is required for homology mode: `brew install blast`.
- Homology workflow verified via `bac2feature --method homology -s test_seqs.fasta -o predicted_traits.tsv`.

## Optional Conda environments
- **Taxonomy (QIIME2)**: use `environment/env_qiime2-2023.5-py39-osx-conda.yml` and create it via  
  `CONDA_SUBDIR=osx-64 conda env create -f environment/env_qiime2-2023.5-py39-osx-conda.yml`.  
  The CLI invokes `conda run --name qiime2-2023.5` internally.
- **Phylogeny (PICRUSt2 stack)**: requires PICRUSt2 plus epa-ng, gappa, taxtastic, FastTree, pplacer, MAFFT, and R packages (ape, castor). Install from bioconda/mamba and run the phylogeny workflow inside that environment.

## Pending / issues
- Taxonomy run currently fails because QIIME2 is not yet installed; upcoming change will surface a clearer error when the command does not produce `taxonomy.tsv`.
- Phylogeny workflow still needs conda-based tooling; not tested in this iteration.
