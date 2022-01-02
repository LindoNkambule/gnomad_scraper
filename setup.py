from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

classifiers = [
    'Development Status :: 1 - Planning',
    'Environment :: Console',
    'Intended Audience :: Science/Research'
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Topic :: Scientific/Engineering :: Bio-Informatics',
    'Operating System :: POSIX',
    'Operating System :: Unix',
    'Operating System :: MacOS'
]

setup(name='gnomad_scraper',
      version='0.1.0',
      author='Lindokuhle Nkambule',
      author_email='lnkambul (at) broadinstitute.org',
      url='',
      description='A command line tool for getting summary stats from the gnomAD browser',
      long_description=long_description,
      long_description_content_type="text/markdown",
      license='MIT',
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'gnomad_scraper = scrapers.main_script:main'
          ]
      },
      classifiers=classifiers,
      keywords='',
      install_requires=['tabulate', 'requests'],
      zip_safe=False
      )