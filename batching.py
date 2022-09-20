def batched_review_rep(reviews,max_len):
  batch_size=len(reviews)
  len_word_vec=len(words)
  rep=torch.zeros(batch_size,max_len)
  for rev_index,review in enumerate(reviews):
    diff_len=max_len-len(review)
    for word_seq, word in enumerate(review):
      rep[rev_index][word_seq+diff_len]=words.index(word)
  return rep.to(torch.long)

def dataloader(npoints,X_,Y_):
  to_ret=[]
  for i in range(npoints):
    index=np.random.randint(len(X_))
    sen,senti=X_[index],Y_[index]
    to_ret.append((sen,senti))
  return to_ret
  
def batched_dataloader(n_points,X_,Y_,verbose=False,device='cpu'):
  len_X_=len(X_)
  reviews=[]
  ratings=[]
  reviews_len=[]
  for i in range(n_points):
    index=np.random.randint(len_X_) 
    review,rating=X_[index],Y_[index] 
    reviews_len.append(len(review))
    reviews.append(review)
    ratings.append(rating)
  
  max_len=max(reviews_len)

  reviews_rep=batched_review_rep(reviews,max_len).to(device)
  ratings_rep=torch.tensor(ratings).to(device)

  if verbose:
    print("Reviews Shape",np.array(reviews).shape)
    print("Padded Review Shape",reviews_rep.shape)
    print("\n\n")

  if verbose:
    print(reviews)
    print(realize_batch_parse(reviews_rep))
    print('--------')

  return reviews,ratings,reviews_rep,ratings_rep,torch.tensor(reviews_len)
