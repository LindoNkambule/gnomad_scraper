#!/usr/bin/env python3

__author__ = 'Lindo Nkambule'

import requests
import sys
from tabulate import tabulate


def print_variant_sum(stats: dict = None):
    var_id = stats['data']['variant']['variantId']
    ref = stats['data']['variant']['reference_genome']
    rsids = stats['data']['variant']['rsids']
    print(f'Variant ID: {var_id}\nReference Genome: {ref}\nRSIDS: {rsids}')

    ex_gen = ['exome', 'genome']

    global ex, gen
    for i in ex_gen:
        if stats['data']['variant'][i] is None:
            if i == 'exome':
                ex = ['No variant', '', '', '']
            else:
                gen = ['No variant', '', '', '']
        else:
            if len(stats['data']['variant'][i]['filters']) == 0:
                filt = 'Pass'
            else:
                filt = stats['data']['variant'][i]['filters']

            if i == 'exome':
                ex = [filt, stats['data']['variant'][i]['ac'], stats['data']['variant'][i]['an'],
                      stats['data']['variant'][i]['af']]
            else:
                gen = [filt, stats['data']['variant'][i]['ac'], stats['data']['variant'][i]['an'],
                       stats['data']['variant'][i]['af']]

    l1 = ['Filter', ex[0], gen[0]]
    l2 = ['Allele Count', ex[1], gen[1]]
    l3 = ['Allele Number', ex[2], gen[2]]
    l4 = ['Allele Frequency', ex[3], gen[3]]

    print(tabulate([l1, l2, l3, l4], headers=['', 'Exomes', 'Genomes']))


def variant_scraper(gnomad_api: str = None, search_type: str = None, search_term: str = None,
                    gnomad_dataset: str = 'gnomad_r2_1'):
    query_variant_id = """
    {
    variant(%s: "%s", dataset: %s) {
        variantId
        rsids
        reference_genome
        
        exome {
           ac
           an
           af
           filters
        }

        genome {
           ac
           an
           af
           filters
        }
       }

    }
    """

    query = query_variant_id % (search_type, search_term, gnomad_dataset)

    response = requests.post(gnomad_api, data={'query': query})

    results = response.json()

    if 'errors' in results:
        sys.exit(results.get('errors')[0].get('message'))

    else:
        print_variant_sum(stats=results)
