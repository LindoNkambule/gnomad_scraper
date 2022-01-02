#!/usr/bin/env python3

__author__ = 'Lindo Nkambule'

import requests
import sys
from tabulate import tabulate


def constrains_table(stats: dict = None, data_type: str = None):
    if data_type == 'gnomad':
        filt = 'gnomad_constraint'
        x = "GNOMAD CONSTRAINTS"
    else:
        filt = 'exac_constraint'
        x = 'EXAC CONSTRAINTS'

    print('\n\033[4m' + x + '\033[0m\n')

    l1 = ['Synonymous', stats['data']['transcript'][filt]['exp_syn'],
          stats['data']['transcript'][filt]['obs_syn']]

    l2 = ['Missense', stats['data']['transcript'][filt]['exp_mis'],
          stats['data']['transcript'][filt]['obs_mis']]

    l3 = ['pLoF', stats['data']['transcript'][filt]['exp_lof'],
          stats['data']['transcript'][filt]['obs_lof']]

    print(tabulate([l1, l2, l3], headers=['Category', 'Expected SNVs', 'Observed SNVs']))


def print_transcript_sum(stats: dict = None):
    var_id = stats['data']['transcript']['transcript_id']
    ref = stats['data']['transcript']['reference_genome']
    gene_symbol = stats['data']['transcript']['gene']['symbol']
    print(f'Transcript ID: {var_id}\nReference Genome: {ref}\nGene Symbol: {gene_symbol}')

    for i in ['gnomad', 'exac']:
        constrains_table(stats=stats, data_type=i)


def transcript_scraper(gnomad_api: str = None, transcript_id: str = None, ref_genome: str = 'GRCh37'):
    query_transcript_id = """
        {
            transcript(transcript_id: "%s", reference_genome: %s) {
                transcript_id,
                reference_genome,
                gene {symbol}

                gnomad_constraint{
                exp_lof,
                exp_mis,
                exp_syn,
                obs_lof,
                obs_mis,
                obs_syn
                }
                exac_constraint{
                exp_syn,
                exp_mis,
                exp_lof,
                obs_syn,
                obs_mis,
                obs_lof
                }
            }
        }
    """
        
    query = query_transcript_id % (transcript_id.upper(), ref_genome)

    response = requests.post(gnomad_api, data={'query': query})

    results = response.json()

    if 'errors' in results:
        sys.exit(results.get('errors')[0].get('message'))

    else:
        print_transcript_sum(stats=results)
