#This code is based on cross-domain authorship attribution baseline in pan18
import argparse
import json
import os

def init(ds_path,answers_path,n=3,ft=5,classifier='OneVsRest'):
    collection = ds_path + os.sep + 'collection-info.json'
    problems = []
    language = []
    with open(collection, 'r') as f:
        for attrib in json.load(f):
            problems.append(attrib['problem-name'])
            language.append(attrib['language'])
    print(problems)
    print(language)

def main():
     parser = argparse.ArgumentParser()
     parser = argparse.ArgumentParser(description='PAN-18 Baseline Authorship Attribution Method')
     parser.add_argument('-i', type=str, help='Path to the main folder of a collection of attribution problems')
     parser.add_argument('-o', type=str, help='Path to an output folder')
     parser.add_argument('-n', type=int, default=3, help='n-gram order (default=3)')
     parser.add_argument('-ft', type=int, default=5, help='frequency threshold (default=5)')
     parser.add_argument('-c', type=str, default='OneVsRest', help='OneVsRest or OneVsOne (default=OneVsRest)')
     args = parser.parse_args()
     if not args.i:
         print('ERROR: The input folder is required')
         parser.exit(1)
     if not args.o:
         print('ERROR: The output folder is required')
         parser.exit(1)
     init(args.i, args.o, args.n, args.ft, args.c)
if __name__ == "__main__":
    main()


