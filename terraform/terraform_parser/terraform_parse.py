import fileinput
import hcl
#from pprint import pprint

# Specify the file path
FILE_PATH = '/Users/jon/temp/terraformer/some_file.tf'
ZONE_ID = 'ZONE_ID'

# Read the file and replace the text
with fileinput.FileInput(FILE_PATH, inplace=True) as file:
    for line in file:
        line = line.replace('-002E-', '-')
        line = line.replace('-002A-', 'wildcard')
        line = line.replace('_"', '"')
        line = line.replace('_A', 'A')
        line = line.replace('_TXT', 'TXT')
        line = line.replace('_SRV', 'SRV')
        line = line.replace('_MX', 'MX')
        line = line.replace('_NS', 'NS')
        line = line.replace('_SOA', 'SOA')
        line = line.replace('_CNAME', 'CNAME')
        print(line, end='')


# Load the modified file
with open(FILE_PATH, 'r', encoding='utf-8') as fp:
    obj = hcl.load(fp)


# create import statements
import_records = obj['resource']['aws_route53_record']
for record in import_records:
    # pprint(import_records[record])
    print()
    print('import {')
    print(f'  to = aws_route53_record.{record}')
    print(f'  id = "{ZONE_ID}_{import_records[record]["name"]}_{import_records[record]["type"]}"')
    print('}')
