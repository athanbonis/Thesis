import os
import codecs
import csv

directory = os.path.join(os.environ["HOMEPATH"], "Desktop","website-genres-classification","7-genre")

files = []
for d in os.walk(directory):
    for sb in d[1]:
        genrePath = os.path.join(directory,sb)
        for f in os.walk(genrePath):
            for file in f[2]:
                genre = sb
                files.append([os.path.join(genrePath,file),genre])
texts = []   
for v in files:
    f=codecs.open(v[0],'r',encoding="ISO-8859-1")
    texts.append((f.read(),v))
    f.close()

with open( 'websites_genre_dataset' + '.csv', mode='w',encoding="ISO-8859-1") as unknown:
    dataset_writer = csv.writer(unknown, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    dataset_writer.writerow(["label","text"])
    for t in texts:
        text = t[0]
        label = t[1][1]
        dataset_writer.writerow([label.replace(" ", ""),text])
            