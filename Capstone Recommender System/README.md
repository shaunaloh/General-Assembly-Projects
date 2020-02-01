# Capstone: Taobao Recommender System

## Problem Statement
Build a recommendation engine to help users in their selection of suitable items sold in e-Commerce giant, Taobao. Based on the individual user's preference from their buying history, page views, add-to-cart items and favorite items, the recommender will output the top 10 most suitable products for each user. 

## Data Set
Data was downloaded from Alibaba Cloud (URL: https://tianchi.aliyun.com/dataset/dataDetail?dataId=649). It includes user behavior data from 25 November 2017 to 3 December 2017.

## Executive Summary
- Data extraction and cleaning
- Exploratory data analysis
- Recommender System
- Model Evaluation

## Approach
Data: The data comprised of implicit taobao's customer information such as user ID, item ID, category ID, user behavior type and date.
Feature Engineering: Data was cleaned and all features was selected as they were all required as inputs to the final recommendation engine.

Model: Alternating Least Squares (ALS). A baseline model was represented by obtaining the most popular items from collated user behavior data.

Evaluation: The AUC score was computed for the individual users, and the mean AUC score was used to compare the baseline with the recommender system.

## Conclusion

Based on a total of 4831 users producing 483,829 user behavioral actions, an implicit recommendation system was implemented to generate the top 10 most suitable items for each user, based on item and user similarity, as well as the interaction scores each user has with the items interacted. The mean AUC score of the ALS model (0.928) was significantly higher than the mean AUC score of the baseline model (0.666).

Relevant information which could be useful for future recommendation systems:
- Price of each item
- Name of each item and category
- User behavior on special dates (e.g. 11.11, Black Friday, Valentine's Day)
- Explicit data (e.g. user review and rating)

## Telegram Bot

I created a telegram bot (@mytaobao2020) to faciliate the recommendations to users with telegram app. This bot aims to help personalize recommendations for each user so that it provides greater efficiency and improves the overall user experience in navigating the actual taobao website.

The commands are: 
- '/start': to start the bot
- '/register': registration is required for new users
- '/help': to provide assistance to the user in using the bot
- '/links': photos and URLs to the top 10 most popular items on taobao website
- '/exit': to leave the bot chat

The bot starts with it's home page and seeks to address the user by his/her name for a more personalized experience. The bot then prompts the user to input his/her user id. For existing users, they will be recommended the top 10 items for purchase based on their user preferences history. For new users, they will be asked to register a new user ID, and the bot will recommend the top 10 most hot selling items. Users will be prompted by the bot to key in their user id, so that the bot can return the list of recommended items. If users key in an invalid user id, the bot will inform the users to key in a valid user id so that it can begin it's recommendation.

The user may also use the commands at anytime during the use of the bot. The commands are included to enhance the overall user experience.

## Herokuapp

The telegram bot is also hosted on herokuapp (@mytaobao_heroku) for users to access the bot on-demand.
