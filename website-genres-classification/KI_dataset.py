import os
import codecs
import csv

directory = os.path.join(os.environ["HOMEPATH"],"Desktop","KI-04")

texts = []
for f in os.listdir(directory):
    f = codecs.open(f,'r',encoding="ISO-8859-1")
    texts.append([f.split('_')[0],f.read()])
    f.close()
print(texts)
