from fastai.text import *
import os

path = "answers" + os.sep
df = pd.read_csv(path + 'ds0.csv')

data_lm = TextLMDataBunch.from_csv(path, 'ds0.csv', text_cols=0, label_cols=1)
data_clas = TextClasDataBunch.from_csv(path, 'ds0.csv', vocab=data_lm.train_ds.vocab, bs=42, text_cols=0, label_cols=1)
moms = (0.8,0.7)
learn = language_model_learner(data_lm, AWD_LSTM)
learn.unfreeze()
learn.fit_one_cycle(4, slice(1e-2), moms=moms)
learn.save_encoder('enc')
learn = text_classifier_learner(data_clas, AWD_LSTM)
learn.load_encoder('enc')
learn.fit_one_cycle(4, moms=moms)
learn.unfreeze()
learn.fit_one_cycle(8, slice(1e-5,1e-3), moms=moms)
test = "still wearing a cool smile. He turned it on the adder in his hand.“ That’s quite enough, Blackscale.”XXX “You- you speak parseltongue, Professor?” “I do. Something I picked up in my travels. It has its uses, as I’m sure you can attest.” Quirrel passed Blackscale back to her. Harry took him with numb hands, returning him to around her neck. Blackscale no longer hung limply; he was coiled now, attentive to the wizard in the room."

learn.predict(test)