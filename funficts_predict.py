#This code is based on cross-domain authorship attribution baseline in pan18
import argparse
import json
import os
import glob
import codecs
from fastai.text import *

def read_files(path,label):
    # Reads all text files located in the 'path' and assigns them to 'label' class
    files = glob.glob(path+os.sep+label+os.sep+'*.txt')
    texts=[]
    for i,v in enumerate(files):
        f=codecs.open(v,'r',encoding='utf-8')
        texts.append((f.read(),label))
        f.close()
    return texts

def init(ds_path,answers_path,n=3,ft=5,classifier='OneVsRest'):
    collection = ds_path + os.sep + 'collection-info.json'
    problems = []
    language = []
    with open(collection, 'r') as f:
        for attrib in json.load(f):
            problems.append(attrib['problem-name'])
            language.append(attrib['language'])
    
    for idx,problem in enumerate(problems):
        if(idx != 0):
            return
        problemInfo = ds_path + os.sep + problem + os.sep + "problem-info.json"
        candidates = []
        with open(problemInfo, 'r') as f:
            jsonFile = json.load(f)
            #unknownFolder = jsonFile['uknown-folder']
            for attrib in jsonFile['candidate-authors']:
                candidates.append(attrib['author-name'])
        train_docs=[]
        for candidate in candidates:
            train_docs.extend(read_files(ds_path+os.sep+problem,candidate))
        train_texts = [text for i,(text,label) in enumerate(train_docs)]
        train_labels = [label for i,(text,label) in enumerate(train_docs)]
        train_data = list(zip(train_texts,train_labels))

        
        
        with open('answers' + os.sep + 'ds' + str(idx) + '.csv', mode='w') as employee_file:
            #getting the number of text for each author
            author_counters = [0] * len(candidates)
            counter = 0
            for i in range(0,len(train_data)):
                if i != 0:
                    if train_data[i][1] != train_data[i-1][1]:
                        counter += 1
                author_counters[counter] += 1
            #writes to csv
            employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            employee_writer.writerow(["label", "text"])
            counter = 0
            local_counter = 0
            for row in train_data:
                is_valid = False
                index = train_data.index(row)
                if(index > 0):
                    if(train_data[index][1] != train_data[index-1][1]):
                            counter += 1
                            local_counter = 0
                if (counter != 20 and local_counter/author_counters[counter] > 0.7):
                    is_valid = True
                employee_writer.writerow([row[1], row[0]])
                local_counter += 1

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


