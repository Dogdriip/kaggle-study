#%%
import pandas as pd
import matplotlib.pyplot as plt
import missingno as msno
from keras import models, layers, optimizers, utils

#%%
training = pd.read_csv('../input/train.csv')
testing = pd.read_csv('../input/test.csv')

#%%
