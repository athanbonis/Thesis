#%% [markdown]
# # This is a test implementation using ULMFiT for text-mining

#%%
from fastai.text import * #NLP Library of ULMFiT

#%% [markdown]
# ### Untar_data will decompress the data file and download it while download_data will just download and save the compressed file in .tgz format.

#%%
path = untar_data(URLs.IMDB_SAMPLE) ##IMDB_SAMPLE is the dataset that we will use
path


#%%
#initialize a dataframe with texts.csv file from IMDB_SAMPLE dataset
df = pd.read_csv(path/'texts.csv', header=None)
df.head() #head will return the first parts of the dataframe


#%%
data_lm = TextLMDataBunch.from_csv(path, 'texts.csv')
data_clas = TextClasDataBunch.from_csv(path, 'texts.csv', vocab=data_lm.train_ds.vocab, bs=42)


#%%
moms = (0.8,0.7)


#%%
learn = language_model_learner(data_lm, AWD_LSTM)
learn.unfreeze()
learn.fit_one_cycle(4, slice(1e-2), moms=moms)


#%%
learn.save_encoder('enc')


#%%
learn = text_classifier_learner(data_clas, AWD_LSTM)
learn.load_encoder('enc')
learn.fit_one_cycle(4, moms=moms)


#%%
learn.unfreeze()
learn.fit_one_cycle(8, slice(1e-5,1e-3), moms=moms)


#%%



