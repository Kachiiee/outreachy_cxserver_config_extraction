#!/usr/bin/python
import csv
import os
import yaml

from pairs_and_engine import Pairs_and_engine
from transform import TransformLanguages

# Get the list of all the files to parse
files = os.listdir('config_files/')
# Translation pair and preferred engine
pair_and_eng = Pairs_and_engine()
# Create a new file - supported_language_pairs
with open('supported_language_pairs.csv', 'w', newline='') as csv_file:
  fieldnames = ['SOURCE LANGUAGE', 'TARGET LANGUAGE', 'TRANSLATION ENGINE', 'IS PREFERRED ENGINE?']
  writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
  # Write the headers
  writer.writeheader()
  # Read all files from files
  for file in files:
    # Files to be ignored
    ignore_files = ['MWPageLoader.yaml', 'languages.yaml', 'mt-defaults.wikimedia.yaml']
    # Ignore the file if present in ignore_files
    if file in ignore_files:
      continue
    # Read the file content
    filename = f'config_files/{file}'
    with open(filename) as fp:
      if (file.split('.')[1] == 'yaml'):
        document = yaml.safe_load(fp)
        # Tranform the language if file has handler with TranformLanguages handler
        if document.get('handler') :
          transform = TransformLanguages(document)
          document = transform.languages
        # Get the language information from document
        for key, value in document.items():
          for lan in value:
            pair = f'{key}-{lan}' # Language pairs
            default_engine = pair_and_eng.get(pair) # Default engine
            preferred_engine = file.split('.')[0] # Preferred engine
            trans_eng = True if default_engine == preferred_engine else False
            # Write the contents in rows
            writer.writerow({'SOURCE LANGUAGE': key, 'TARGET LANGUAGE': lan, 'TRANSLATION ENGINE': preferred_engine, 'IS PREFERRED ENGINE?': trans_eng})
