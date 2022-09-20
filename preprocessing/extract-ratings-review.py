df=pd.read_csv('/content/zomato.csv')


def remove_url(data):
  return re.sub(r'https\S',' ',data)

#Separate out all the individual reviews of the restaurants
split_reviews=removed_web.apply(lambda x: x[9:].split(', (\'Rated '))

#Removing Duplicates
split_reviews=split_reviews.apply(lambda x: list(set(x)))

def extract_ratings(x):
  ratings=[]
  for i in x:
    ratings.append(i[:1])
  return ratings

def extract_reviews(x):
  reviews=[]
  for i in x:
    reviews.append(i[14:-2])
  return reviews

#Segregate reviews and ratings
all_ratings=split_reviews.apply(lambda x: extract_ratings(x))
all_reviews=split_reviews.apply(lambda x: extract_reviews(x))  

#flatten out ratings and reviews
rating_list=[rating for restaurant_ratings in all_ratings for rating in restaurant_ratings]
review_list=[review for restaurant_reviews in all_reviews for review in restaurant_reviews]
