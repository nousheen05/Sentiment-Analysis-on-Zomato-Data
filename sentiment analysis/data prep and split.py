#Loading corpus of reviews
with open("/content/drive/MyDrive/working_corpus","rb") as fp:
  corpus=pickle.load(fp)

#Loading all ratings in sequence order of the review corpus
with open("/content/drive/MyDrive/rating_list_working","rb") as fp:
  ratings=pickle.load(fp)

#create dictionary from all the words used in the corpus
dictionary=Dictionary(corpus)

words=[]
words.append('')
for key,value in dictionary.items():
  words.append(value)

#segmenting Ratings value from 1-5 to 0-2 (positive,negative, neutral)
sentiment=[]
for i in ratings:
  if(i<3):
    sentiment.append(0)
  elif (i==3):
    sentiment.append(1)
  else :
    sentiment.append(2)
    
X=corpus.copy()
Y=sentiment.copy()

'''Removing Excess positive sentiment: 
Current number for neg,neu,pos: 28632, 24849, 80415
Target number for neg,neu,pos: 28632, 24849, 30415
THUS remove 50,000 positive instances from dataset'''

count=0
target_removals=50000
for i in range(len(Y)-1,-1,-1):
 if Y[i]==2:
   X.pop(i)
   Y.pop(i)
   count+=1
   if count==target_removals:
     break
     
     
#Split Training, Test and Validation Data
X_train,X_testing,Y_train,Y_testing=train_test_split(X,Y,test_size=0.3,random_state=0,stratify=Y)
X_val,X_test,Y_val,Y_test=train_test_split(X_testing,Y_testing,test_size=0.5,random_state=0,stratify=Y_testing)
