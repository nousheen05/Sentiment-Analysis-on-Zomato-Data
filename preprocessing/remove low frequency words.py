import gensim
from gensim import corpora
from gensim.corpora import Dictionary

review_dct=Dictionary(lemmatized_review)


#Finding frequency of each word in corpus dictionary
corpus = [review_dct.doc2bow(sent) for sent in tqdm(lemmatized_review,desc='Term Frequency')]
vocab_tf_row=[dict(i) for i in corpus]
counter=collections.Counter()
for i in tqdm(vocab_tf_row,desc='Accumulating Frequencies'):
  counter.update(i)
  #converting counter object to dictionary object 
res=dict(counter)


#Creating list of rare words and index having frequency less than 5 in the corpus
#Creating list of rare words and index having frequency more than or equal to 5 in the corpus
working_words_ids=[]
rare_words_ids=[]
for i,j in tqdm(res.items(),desc='Counting low Frequent indices'):
  if j<5:
    rare_words_ids.append(i)
  else:
    working_words_ids.append(i)

    
#Remove rare words from dictionary
working_words=[review_dct[i] for i in working_words_ids]
rare_words=[review_dct[i] for i in rare_words_ids]
