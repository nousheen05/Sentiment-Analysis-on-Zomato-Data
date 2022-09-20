#Initializing BiLSTM model instance with appropriate parameters
word_size=len(words)
n_hidden=256
num_layers=2
embedding_dim=100
net_BiLSTM=BiLSTM_net(word_size,n_hidden,num_layers,output_size=3,embedding_dim=embedding_dim,dropout=0.5)

#Importing glove model
!wget http://nlp.stanford.edu/data/glove.6B.zip
!unzip glove.6B.zip

#using glove.6B.100d embeddings
with open('glove.6B.100d.txt','rt') as fi:
    pretrained_glove_emb = fi.read().strip().split('\n')

#Obtain word and their embedding in separate lists
vocab,embeddings=[],[]
for i in range(len(pretrained_glove_emb)):
    word = pretrained_glove_emb[i].split(' ')[0]
    emb = [float(val) for val in pretrained_glove_emb[i].split(' ')[1:]]
    vocab.append(word)
    embeddings.append(emb)
    
#Using only those word embeddings which are present in the corpus and glove pretrained model
for index,word in enumerate(words):
  if word in vocab:
    ind=vocab.index(word)
    emb=torch.tensor(embeddings[ind])
    net_BiLSTM.embedding.weight.data[index]=emb
