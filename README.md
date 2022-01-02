# gnomAD scraper

A python command-line "mini" package for querying the gnomAD browser by variant ID, rsid, transcript ID, or gene ID/Symbol using the gnomAD API.

## Installation

Install gnomad_scraper directly from GitHub.

```bash
pip3 install git+https://github.com/LindoNkambule/gnomad_scraper.git
```

## Usage
Users can query **variants**, **genes**, and **transcripts** from gnomAD broswer. Below are examples

### 1. Variants ###
Variants can be queried using:
1. Variant ID
```bash
gnomad_scraper --type variant_id --search-by 15-28414666-G-A
```
2. RDIS
```bash
gnomad_scraper --type rsid --search-by rs201857604
```

Searching some variants by rsid might lead to a 'Multiple variants found, query using variant ID to select one.'
message.


### 2. Genes ###
Genes can be queried using:
1. Gene ID
```bash
gnomad_scraper --type gene_id --search-by ENSG00000169174
```
2. Gene Symbol/ Name
```bash
gnomad_scraper --type gene_symbol --search-by PPARA
```


### 3. Transcripts ###
Transcripts can be queried using transcript id
```bash
gnomad_scraper --type transcript_id --search-by ENST00000302118
```

## Arguments and Options
**Argument** | **Description**
--- | ---
``--type`` | Type of information to query the gnomAD browser by. Options: **[variant_id, gene_id, gene_symbol, rsid, transcript_id]**
``--search-by`` | Keyword to query gnomAD browser by
``--ref-genome`` | Reference genome to use. Default is GRCh37. Options: **[GRCh37, GRCh38]**
``--dataset`` | Dataset to search from. Default is gnomad_r2_1. Options: **[gnomad_r2_1, gnomad_r3, exac, gnomad_r2_1_non_neuro, gnomad_r2_1_non_cancer, gnomad_r2_1_non_topmed, gnomad_r2_1_controls]**



## WHAT'S COMING
We're going to implement a feature for querying the gnomAD broswer using information
from a text file and annotating the file with queried information

**If there's a feature you'd like to have, please open an issue detailing the feature.**