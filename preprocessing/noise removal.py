#Removing non numeric ratings along with their reviews
#pop-ing in reverse order of the index
for i in non_numeric_rating[::-1]:
  rating_list.pop(i)
  review_list.pop(i)
  
#Convert rating value from String to Integer datatype
rating_list=list(map(int,rating_list))



#Remove punctuation
def remove_punc(contents):
  punc_list=(string.punctuation).replace
  table=contents.maketrans(string.punctuation,' ' * len(string.punctuation))
  return contents.translate(table)
  
#Remove white spaces
def remove_white_space(data):
  return ' '.join(data.split())

#Remove word containing non ascii characters
def remove_non_ascii_words(contents):
  string_ascii = ' '.join([ token for token in contents.split() if token.isascii() ])
  return string_ascii

#Noise Removal
def remove_noise(contents):
  remove_pun=remove_punc(contents)
  remove_spaces=remove_white_space(remove_pun)
  remove_non_ascii=remove_non_ascii_words(remove_spaces)
  return remove_non_ascii

review_no_noise=[remove_noise(i) for i in review_list]

