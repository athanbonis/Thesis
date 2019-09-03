import os
import codecs
import csv

directory = os.path.join("C:/","GitHub","Thesis","website-genres-classification","KI-04")

texts = []
for txtfile in os.listdir(directory):
    f = codecs.open(os.path.join(directory,txtfile),'r',encoding="ISO-8859-1")
    texts.append([txtfile.split('_')[0],f.read()])
    f.close()
print(texts)

with open('KI-04.csv',mode='w',encoding="ISO-8859-1") as ds:
    dataset_writer = csv.writer(ds, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    dataset_writer.writerow(["label","text"])
    for t in texts:
        label = t[0]
        text = t[1]
        dataset_writer.writerow([label,text])