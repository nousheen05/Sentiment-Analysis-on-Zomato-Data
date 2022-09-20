import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import torch
import seaborn as sns
import re
import nltk
from itertools import groupby
from tqdm import tqdm,tqdm_notebook
from warnings import filterwarnings
filterwarnings('ignore')

import collections
import functools
import operator

#For part of speech tagging
import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('omw-1.4')

import inflect
import gensim
from gensim import corpora
from gensim.corpora import Dictionary
from gensim.utils import lemmatize
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer
from nltk.corpus.reader import wordnet
from bs4 import BeautifulSoup
import re, string, unicodedata
