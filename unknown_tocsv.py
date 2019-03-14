import csv
import codecs
import glob 
import os
import json

def read_files(path,label):
    # Reads all text files located in the 'path' and assigns them to 'label' class
    files = glob.glob(path+os.sep+label+os.sep+'*.txt')
    texts=[]
    for i,v in enumerate(files):
        #if(i < 4):
            print(i)
            f=codecs.open(v,'r',encoding='utf-8')
            texts.append((f.read(),label))
            f.close()
    return texts

def main():
    collection = 'pan18' + os.sep + 'collection-info.json'
    problems = []
    with open(collection, 'r') as f:
        for attrib in json.load(f):
            if(len(problems) < 4):
                problems.append(attrib['problem-name'])
    print(problems)
    for idx,problem in enumerate(problems):
        
    #f = open("pan18/problem00001/unknown/unknown00001.txt", "r")
    #texts = []
    #texts.append(f.read())
    #with open('unknown_ds.csv', mode='w') as unknown:
     #   unknown_writer = csv.writer(unknown, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      #  unknown_writer.writerow(texts)

if __name__ == "__main__":
    main()