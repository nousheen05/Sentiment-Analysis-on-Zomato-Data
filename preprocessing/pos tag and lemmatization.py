#POS tagging of the review words
pos_tag=[]
for i in tqdm(unique,desc='POS Tagging'):
  pos_tag.append(nltk.pos_tag(i))
  
  
#Limiting the working POS word tags to Adjective, Verb, Noun, Adverb
def pos_tagger(nltk_tag):
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV

#POS tagging each words in reviews using the above four POS-tags
wordnet_tagged=[]
for i in tqdm(pos_tag,desc='Tag conversion'):
  wordnet_tagged.append(list(map(lambda x: (x[0], pos_tagger(x[1])), i)))
  
  
  
def lemmatization(contents):
  lem = WordNetLemmatizer()
  lem_list=[]
  for i in tqdm(contents,desc='Lemmatization'):
    lem_review=[]
    for j in i:
      if j[1] is None:
        lem_review.append(j[0])
      else:
        lem_review.append(lem.lemmatize(j[0],j[1]))
    lem_list.append(lem_review)
  return lem_list
  
lemmatized_review=lemmatization(wordnet_tagged)
