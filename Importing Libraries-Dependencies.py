import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import seaborn as sns

import os, string, random, time, math
from tqdm.notebook import tqdm
import time

from sklearn.model_selection import train_test_split
import sklearn.preprocessing as preprocessing
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

import gensim
from gensim import corpora
from gensim.corpora import Dictionary

from torch.cuda import is_available
import torch 
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

device_gpu=torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

from IPython.display import clear_output
