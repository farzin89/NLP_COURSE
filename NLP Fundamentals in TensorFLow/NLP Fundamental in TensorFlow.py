"""NLP Fundamental in Tensorflow.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gnG6K79et9WLTrlNE2C8Rle_29TCis8r

# Introduction to NLP Fundamentals in TensorFlow

NLP has the goal of deriving information out of natural language (could be sequences Text or speech). Another common term for NLP problems is sequence to sequence problems(seq2seq)

## check for GPU
"""

!nvidia-smi =L

"""##Get helper function"""

!wget https://raw.githubusercontent.com/mrdbourke/tensorflow-deep-learning/main/extras/helper_functions.py

# Import series of helper functions for the notebook

from helper_functions import unzip_data,create_tensorboard_callback,plot_loss_curves,compare_historys



"""## Get a text dataset 

The dataset we're going to be using is Kaggle's introduction to NLP dataset(text samples of Tweeets labelled as disaster or not disaster).

see the original source here: https://www.kaggle.com/competitions/nlp-getting-started/data
"""

!wget https://storage.googleapis.com/ztm_tf_course/nlp_getting_started.zip

# Unzip data

unzip_data("nlp_getting_started.zip")

"""## Visualizing a text dataset 

To visualize our text samples, we first have to read them in, one way to do so would be to use Python : https://realpython.com/read-write-files-python/

But I prefer to get visual straight away. 
So another way to do this is to use pandas.. 
"""

import pandas as pd

train_df = pd.read_csv("train.csv")
test_df = pd.read_csv("test.csv")
train_df.head()

train_df["text"][1]

# shuffle training dataframe

train_df_shuffled = train_df.sample(frac=1,random_state=42)
train_df_shuffled.head()

# What does the test dataframe look like?

test_df.head()

# How many examples of each class?
train_df.target.value_counts()

# How many total samples?

len(train_df),len(test_df)

# Let's visualize some random training examples

import random
random_index = random.randint(0,len(train_df)-5) # create random indexs not higher than the total number of samples
for row in train_df_shuffled[["text","target"]][random_index:random_index+ 5 ].itertuples():
  _,text,target = row
  print(f"Target: {target}","(real disaster)" if target > 0 else "(not real disaster)")
  print(f"Text:\n{text}\n")
  print("---\n")