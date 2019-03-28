import csv
import codecs
import glob 
import os
import json

def main():
    collection = 'pan18' + os.sep + 'datasets' + os.sep + 'collection-info.json'
    problems = []
    with open(collection, 'r') as f:
        for attrib in json.load(f):
            if(len(problems) < 4):
                problems.append(attrib['problem-name'])
    for idx,problem in enumerate(problems):
        path_unknown = 'pan18' + os.sep + problem + os.sep + 'unknown'
        files = os.listdir(path_unknown)
        with open( 'unknown_dsets' + os.sep + 'unknown_ds'+ str(idx) + '.csv', mode='w') as unknown:
            unknown_writer = csv.writer(unknown, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for name in files:
                f = open(path_unknown + os.sep + name, "r")
                texts = []
                texts.append(f.read())
                unknown_writer.writerow(texts)
if __name__ == "__main__":
    main()
