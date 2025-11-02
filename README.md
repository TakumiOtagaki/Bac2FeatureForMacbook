# はじめに
これは私が自分の MacBook で利用したくて改変したものなので、あまり信用して利用しないでください。
Please note that this repo is a modified version for my local MacBook environment, and may not be reliable.

# Bac2Feature

![version](https://img.shields.io/badge/version-1.1-blue)

> [!WARNING]  
> Bac2Feature web service is currently stopped due to server migration. Please wait for a few weeks.

Bac2Feature is an easy-to-use interface to predict bacterial and archaeal traits from 16S rRNA gene sequences.

Bac2Feature integrates three representative methods for trait prediction and provided them with systematic evaluations for avoiding spurious predictions. See Citations for details.
## Predicted traits by Bac2Feature
Currently, Bac2Feature predicts 8 continuous and 10 categorical traits listed below.
- Continuous traits
	- Doubling time (log_10 hours)
	- Growth temperature (degrees C)
	- Optimum growth temperature (degrees C)
	- Genome size (base pair)
	- GC content (percentage)
	- Coding genes (number)
	- rRNA 16S genes (number)
	- tRNA genes (number)
- Categorical traits (All traits are predicted yes (=1) or no (=0).)
	- Gram stain
	- Sporulation
	- Anaerobes
	- Motility
	- Temperature range
		- Mesophiles, Thermophiles
	- Cell shape
		- Bacillus, Coccus, Filament, Spiral
## Download stand-alone version
Bac2Feature is currently supported on Linux-based operating systems and has been verified on Ubuntu 22.04 LTS, 24.04 LTS and Red Hat Enterprise Linux 8.7.
```sh
# Clone github repository
git clone https://github.com/fuyo780/Bac2Feature.git
cd Bac2Feature/

# Add Conda repositories, if necessary
conda config --append channels conda-forge
conda config --append channels bioconda

# Create Conda environment
#   Linux:
conda create --name bac2feature --file environment/env_bac2feature.txt
#   macOS (avoids Linux-only packages; tested on Apple silicon):
conda env create --name bac2feature --file environment/env_bac2feature_macos.yml
#   Apple silicon tip (Rosetta x86_64 build):
#     export CONDA_SUBDIR=osx-64
#     conda env create --name bac2feature --file environment/env_bac2feature_macos.yml
#     unset CONDA_SUBDIR

# Activate environment (after creation)
conda activate bac2feature

# (Optional) Create Conda environment for taxonomy-based prediction
# Linux:
conda create --name qiime2-2023.5 --file environment/env_qiime2-2023.5-py38-linux-conda.txt
# macOS:
#   export CONDA_SUBDIR=osx-64
#   conda env create --file environment/env_qiime2-2023.5-py39-osx-conda.yml
#   unset CONDA_SUBDIR

# Install Bac2Feature command line (execute at this directory Bac2Feature)
pip install bac2feature
# or with uv (https://github.com/astral-sh/uv)
uv pip install bac2feature
# For local development using uv:
# uv venv .venv && source .venv/bin/activate && uv pip install -e .

# Quick smoke test (homology method does not require PICRUSt2):
bac2feature --method homology -s test_seqs.fasta -o predicted_traits.tsv

# The homology method requires the BLAST+ command-line tools. On macOS you can install them with:
#   brew install blast
# or with conda/mamba:
#   conda install -c bioconda blast

# The phylogeny-based prediction requires additional tooling that is not available on PyPI,
# including PICRUSt2 (install via `mamba install -c bioconda picrust2`), epa-ng, gappa,
# and R packages (castor, ape). Run `bac2feature --method phylogeny ...` only inside an
# environment where these tools are installed.

# Print help message
bac2feature -h

# Usage example
bac2feature -s test_seqs.fasta -o predicted_traits.tsv

```
## Citations
Bac2Feature: an easy-to-use interface to predict prokaryotic traits from 16S rRNA gene sequences  
Masaki Fujiyoshi, Takao K Suzuki, Wataru Iwasaki, Chikara Furuwasa, Motomu Matsui. Bioinform. Adv., 2025.
## Contact
- Masaki Fujiyoshi (The University of Tokyo): fujiyoshi-masaki353@g.ecc.u-tokyo.ac.jp
- [Matsui Motomu](https://sites.google.com/site/motomumatsui/) (Kyoto University): motomu.matsui@gmail.com
