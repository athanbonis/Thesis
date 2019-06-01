from fastai.text import *
from fastai.core import *
from fastai import *
import os

path = 'answers' + os.sep
df = pd.read_csv(path +'ds0.csv')
print(df.head())
data_lm = TextLMDataBunch.from_csv(path,"ds0.csv")
data_clas = TextClasDataBunch.from_csv(path, "ds0.csv", vocab=data_lm.train_ds.vocab, bs=42)
data_lm.save('data_lm_export.pkl')
data_clas.save('data_clas_export.pkl')
learn = language_model_learner(data_lm, AWD_LSTM, drop_mult=0.5)
learn.fit_one_cycle(1, 1e-2)
learn.unfreeze()
learn.fit_one_cycle(1, 1e-3)

