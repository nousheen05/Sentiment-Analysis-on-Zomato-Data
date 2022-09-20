#text to lower case
def to_lower(contents):
  return contents.lower()
#tokenize words
nltk.download('punkt')
def tokenize(contents):
  return nltk.word_tokenize(contents)
#remove_stopwords
nltk.download('stopwords')
def remove_stopwords(contents):
  cachedStopWords = stopwords.words("english")[:121]
  include_words=['until','above','below','down','up','under','over','out','why','how','all','any','both','each']
  for i in include_words:
    cachedStopWords.remove(i)
  no_stopwords=[]
  for i in tqdm(contents,desc='Stopword Removal'):
    no_stopwords.append([j for j in i if j not in cachedStopWords])
  return no_stopwords
tokens=[]
for i in review_no_noise:
  review_tolower=to_lower(i)
  tokens.append(nltk.word_tokenize(review_tolower))
no_stopwords=remove_stopwords(tokens)
