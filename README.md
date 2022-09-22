# Exploratory Data Analysis on Zomato Data

## Overview
The project uses data of customer reviews and ratings of restaurants in Bangalore (listed on Zomato), to make a model that could predict correct sentiment from a review.

## Blog on the Project

Preprocessing: [Data Preprocessing for Sentiment Analysis on Zomato Reviews](https://linktodocumentation)

Network Design and Training: [Sentiment Analysis on Zomato Reviews](https://medium.com/@Tan_D/sentiment-analysis-on-zomato-reviews-4bc841e4b040) 

## Motivation

Reviews are related with almost every brand product or service. Sometimes it becomes necessary for a business to know how a product is being recognized by their customer. Thus, sentiment analysis which classifies text to a particular sentiment comes to help in identifying the sentiment associated with customer description of a product or service.
 

## Task

We divide the task for this project into:
- Preprocessing: Extract the raw text from the source, and make necessary transformation and tuning to turn it to a form which works well for our model.
- Network Architecture and Training: Design our network and set up training methods which helps in building a robust sentiment analysis model. 

## About Data

- The Zomato dataset has 51717 instances of 17 features/columns. Out of these, only one is numeric type.
- The corpus obtained after Preprocessing has pairs of 133896 ratings and reviews.

![info](https://user-images.githubusercontent.com/35737849/191679179-f93be4b3-45d0-45e3-b2f7-ebcd3ae40121.PNG)
<br/>
## Roadmap

Preprocessing:

- Review-Rating extraction from source data

- Textual Noise removal
- Text Normalization
- Lemmatization
- Lower frequency word removal
- Data balancing

Network Design and Training:

- Model Design (BiLSTM)

- Set up Training for Model

- Implement Batching

- Use Pre-trained embedding(glove) to the model

- Train and Evaluate model


## Tech Stack

- Pytorch
- pandas
- matplotlib
- numpy
- scikit learn
- nltk



## Acknowledgements/Credits

 The source data belongs to Zomato Ltd. and is extracted by [Himanshu Poddar](https://github.com/poddarhimanshu).
 Please give necessary credits if you are using the data.
