#!/usr/bin/env python3

__author__ = 'Lindo Nkambule'

import requests
import sys
from tabulate import tabulate


def gene_constrains_table(stats: dict = None, data_type: str = None):
    if data_type == 'gnomad':
        filt = 'gnomad_constraint'
        x = "GNOMAD CONSTRAINTS"
    else:
        filt = 'exac_constraint'
        x = 'EXAC CONSTRAINTS'

    print('\n\033[4m' + x + '\033[0m\n')

    ref = stats['data']['gene']['reference_genome']

    if stats['data']['gene']['gnomad_constraint'] is None:
        print(f'Constraint not yet available for {ref}')
    elif stats['data']['gene']['exac_constraint'] is None:
        print(f'Constraint not yet available for {ref}')
    else:
        l1 = ['Synonymous', stats['data']['gene'][filt]['exp_syn'],
              stats['data']['gene'][filt]['obs_syn']]

        l2 = ['Missense', stats['data']['gene'][filt]['exp_mis'],
              stats['data']['gene'][filt]['obs_mis']]

        l3 = ['pLoF', stats['data']['gene'][filt]['exp_lof'],
              stats['data']['gene'][filt]['obs_lof']]

        print(tabulate([l1, l2, l3], headers=['Category', 'Expected SNVs', 'Observed SNVs']))


def print_gene_sum(stats: dict = None):
    gene_id = stats['data']['gene']['gene_id']
    ref = stats['data']['gene']['reference_genome']
    gene_symbol = stats['data']['gene']['symbol']
    print(f'Gene ID: {gene_id}\nReference Genome: {ref}\nGene Symbol: {gene_symbol}')

    for i in ['gnomad', 'exac']:
        gene_constrains_table(stats=stats, data_type=i)


def gene_scraper(gnomad_api: str = None, gene_search_method: str = None, search_term: str = None,
                 ref_genome: str = 'GRCh37'):
    query_gene = """
        {
            gene(%s: "%s", reference_genome: %s) {
                gene_id
                reference_genome
                symbol

                gnomad_constraint {
                exp_lof
                exp_mis
                exp_syn
                obs_lof
                obs_mis
                obs_syn
                }

                exac_constraint {
                exp_syn
                exp_mis
                exp_lof
                obs_syn
                obs_mis
                obs_lof
                }
            }
        }
    """

    query = query_gene % (gene_search_method, search_term.upper(), ref_genome)

    response = requests.post(gnomad_api, data={'query': query})

    results = response.json()

    if 'errors' in results:
        sys.exit(results.get('errors')[0].get('message'))

    else:
        print_gene_sum(stats=results)
