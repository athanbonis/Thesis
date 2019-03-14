from fastai.text import *
from fastai.core import *
from fastai import *
import os

#from google.colab import drive
#drive.mount('/content/drive')

#path = "/content/drive/My Drive/Colab Notebooks/"
path = 'answers' + os.sep
df = pd.read_csv(path + 'ds0.csv')
#df.count
#df1 = pd.read_csv(path + 'ds1.csv')
#df2 = pd.read_csv(path + 'ds2.csv')
#df3 = pd.read_csv(path + 'ds3.csv')
#df.append(df1)
#df.append(df2)
#df.append(df3)
#df.shape

test = pd.read_csv(path + 'unknown_dsets/unknown_ds0.csv')
#test_df.count
#test_df1 = pd.read_csv(path + 'unknown_dsets/unknown_ds1.csv')
#test_df2 = pd.read_csv(path + 'unknown_dsets/unknown_ds2.csv')
#test_df2 = pd.read_csv(path + 'unknown_dsets/unknown_ds3.csv')
#test

data_lm = TextLMDataBunch.from_df(path,train_df=df,valid_df=df,test_df=test,text_cols=0,label_cols=1)
#data_lm = TextLMDataBunch.from_csv(path, 'ds0.csv', text_cols=0, label_cols=1)
data_clas = TextClasDataBunch.from_df(path, train_df=df,valid_df=df, vocab=data_lm.train_ds.vocab, bs=42, text_cols=0, label_cols=1)

moms = (0.8,0.7)

learn = language_model_learner(data_lm, AWD_LSTM, drop_mult=0.5)
learn.lr_find()
learn.recorder.plot()

learn.fit_one_cycle(4, slice(1e-01), moms=moms)

learn.unfreeze()
learn.fit_one_cycle(4, slice(1e-01), moms=moms)

learn.save_encoder('enc')

learn = text_classifier_learner(data_clas,AWD_LSTM,drop_mult=0.7)
learn.lr_find()
learn.recorder.plot()

learn.load_encoder('enc')
learn.fit_one_cycle(8,slice(1e-01), moms=moms)

learn.unfreeze()
learn.fit_one_cycle(8, slice(1e-01), moms=moms)

preds = learn.get_preds(True)

print(preds[0])
