#!/usr/bin/env python3

__author__ = 'Lindo Nkambule'

import argparse


def main():
    parser = argparse.ArgumentParser(description='preimp_qc')
    parser.add_argument('--type', type=str, default='variant_id',
                        choices=['variant_id', 'gene_id', 'gene_symbol', 'rsid', 'transcript_id'],
                        help='Search using: `chrom_pos` (variant), `gene_id, `rsid` (variant) or `transcript_id`.')
    parser.add_argument('--search-by', type=str, help='Keyword to search by')
    parser.add_argument('--ref-genome', type=str, default='GRCh37', choices=['GRCh37', 'GRCh38'],
                        help='Reference genome to use')
    parser.add_argument('--dataset', type=str, default='gnomad_r2_1',
                        choices=['gnomad_r2_1', 'gnomad_r3', 'exac', 'gnomad_r2_1_non_neuro', 'gnomad_r2_1_non_cancer',
                                 'gnomad_r2_1_non_topmed', 'gnomad_r2_1_controls'], help='Dataset t search from')

    args = parser.parse_args()

    # Error handling
    types = ['chrom_pos', 'gene_id', 'rsid', 'transcript_id']

    datasets = ['gnomad_r2_1', 'gnomad_r3', 'exac', 'gnomad_r2_1_non_neuro', 'gnomad_r2_1_non_cancer',
                'gnomad_r2_1_non_topmed', 'gnomad_r2_1_controls']

    gnomad_api = 'https://gnomad.broadinstitute.org/api/'

    # Query VARIANT by Variant ID or RSID
    if args.type == 'variant_id' or args.type == 'rsid':
        from scrapers.variant_query import variant_scraper

        if args.type == 'variant_id':
            type_query = 'variantId'
        else:
            type_query = 'rsid'

        # def variant_scraper(gnomad_api: str = None, search_type: str = None, search_term: str = None,
        #                     gnomad_dataset: str = 'gnomad_r2_1'):

        if not args.search_by:
            variant_search_id = '1-55516888-G-GA'
            variant_scraper(gnomad_api=gnomad_api, search_type=type_query, search_term=variant_search_id,
                            gnomad_dataset=args.dataset)
        else:
            variant_scraper(gnomad_api=gnomad_api, search_type=type_query, search_term=args.search_by,
                            gnomad_dataset=args.dataset)

    # Query TRANSCRIPT by TRANSCRIPT ID
    elif args.type == 'transcript_id':
        from scrapers.transcript_query import transcript_scraper
        if not args.search_by:
            transcript_search_id = 'ENST00000302118'
            transcript_scraper(gnomad_api=gnomad_api, transcript_id=transcript_search_id, ref_genome=args.ref_genome)
        else:
            transcript_scraper(gnomad_api=gnomad_api, transcript_id=args.search_by, ref_genome=args.ref_genome)

    # Query GENE by GENE ID or GENE SYMBOL/NAME
    elif args.type == 'gene_id' or args.type == 'gene_symbol':
        from scrapers.gene_query import gene_scraper
        if not args.search_by:
            gene_search_id = 'ENSG00000169174'
            gene_scraper(gnomad_api=gnomad_api, gene_search_method='gene_id', search_term=gene_search_id,
                         ref_genome=args.ref_genome)
        else:
            gene_scraper(gnomad_api=gnomad_api, gene_search_method=args.type, search_term=args.search_by,
                         ref_genome=args.ref_genome)

    else:
        print('Other search methods coming soon!')


if __name__ == '__main__':
    main()
