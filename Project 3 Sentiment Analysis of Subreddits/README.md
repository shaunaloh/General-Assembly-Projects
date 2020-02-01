# Project-3 Web APIs and Classification

## Problem Statement
Using Reddit's API, collect posts from two subreddits of my choosing (r/oculus and r/Vive).

Use NLP to train a classifier model on which subreddit a given post came from.

[Additional] Use sentiment analysis to compare the popularity between Oculus and Vive, which are both Virtual Reality products.

## Executive Summary
1. Data Collection
2. Data Cleaning & EDA
3. Sentiment Analysis
4. Preprocessing and Modelling
5. Model Evaluation
6. Conclusion and Recommendations

## 1. Data Collection
I collected data from 2 subreddits - r/oculus and r/Vive via Pushshift API. A total of 10,000 comments and 6216 comments were collected from Oculus and Vive respectively. The comments were amalgamated into a single dataframe and saved as 'comments.csv'. I chose these 2 subreddits as they have a good amount of text for NLP and were rival products in the same technological chase, and hence suitable for comparison.

## 2. Data Cleaning & EDA
I first checked for null comments, and received output that there are no null fields. I then dropped the following from my dataframe:

- duplicated comments
- [deleted] comments
- [removed] comments

I then proceeded to clean my text by removing non-letters and stop words. I then lemmatized the words and saved the cleaned text as 'clean_comments.csv'.

## 3. Sentiment Analysis

I initiated a Count Vectorizer to retrieve 500 features, as a basis to understand my possible list of positive and negative words. I then referenced an online source: "https://github.com/jeffreybreen/twitter-sentiment-analysis-tutorial-201107/tree/master/data/opinion-lexicon-English" as my library of positive and negative words. I applied sentiment analysis and the results obtained showed that both Oculus and Vive have positive sentiments, with vive having a higher positive sentiment than Oculus (0.0437 vs 0.0285). This provides us an insight into the popularity of Oculus and Vive. 

## 4. Preprocessing and Modelling

I used Tfidf Vectorizer to convert my text to numeric features. Tfidf Vectorizer was chosen because it could penalize common words and provide greater influence on rare words, a trait lacking in Count Vectorizer. A total of 3000 features were used for modelling. I created a baseline logistic regression model, a logistic regression model with stop words and ngram range of 1-2, and a Bayes classifier (Multinomial Naive Bayes Model). I performed Grid Search regularization on my logistic regression model. I did a Confusion Matrix for the logistic regression model and Multinomial Naive Bayes Model to understand the precision, accuracy, sensitivity and specificity of the models. The ROC scores were also calculated to assess my models.

## 5. Model Evaluation

- Baseline Logistic Regression: The train and test scores were close (0.751 vs 0.709). 
- Logistic Regression: The train score was slightly higher than the test score (0.781 vs 0.724). This suggests slight overfitting, hence I performed GridSearchcv and the test score returned was 0.728.
- Multinomial Naive Bayes: The train and test scores were close (0.754 vs 0.713).

Out of the 3 models, the Logistic Regression performed the best with no overfit nor underfit.

## 6. Conclusion and Recommendations
Based on the train and test scores of the Logistic Regression model, it was a relatively well-performing model that could be used to predict if the subreddit belonged to Oculus or Vive. A possible extension to this project could be to explore the upvotes in determining the popularity of the subreddits, and also to scrap a larger dataset to train a more representative prediction model.
