# gnomAD scraper

Query information by variant ID, rsid, transcript, or gene name from the gnomAD browser using the gnomAD API.

## Installation

Clone the repo and install gnomad_scraper and the required packages.

```bash
git clone https://github.com/LindoNkambule/gnomad_scraper.git
cd gnomad_scraper/
pip3 install -r requirements.txt
python3 setup.py sdist
pip3 install dist/gnomad_scraper-0.1.0.tar.gz
```

## Usage
```bash
gnomad_scraper
```
The above command should print out basic stats for Variant ID: 1-55516888-G-GA