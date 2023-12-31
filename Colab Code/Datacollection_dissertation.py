# -*- coding: utf-8 -*-
"""Jenny_dissertation

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V2Ugf71VYOWczD_SfFZbmlLePumFYdMB
"""

!pip install tweepy

!pip install preprocessor

from tweepy import *

import pandas as pd
import csv
import re
import string
#import preprocessor as p


# Due to Twitter policy restrictions, we used multiple Twitter API accounts to pull tweets, as seen in our code.



# Due to privacy concerns, the API keys have been removed. 
# If you're using this code, insert your own API keys in the appropriate places.

 consumer_key = "YOUR_CONSUMER_KEY"
 consumer_secret = "YOUR_CONSUMER_SECRET"
 access_key= "YOUR_ACCESS_KEY"
 access_secret = "YOUR_ACCESS_SECRET"

#Passing in  Twitter API authentication key
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    access_key, access_secret
)

#the tweepy API
api = tweepy.API(auth, wait_on_rate_limit=True)


search_query = ["i'm depressed", "loneliness", "feeling sad", "feel angry", "lonely","mental well-being", "Suicidal","want to die","Mental health" , "self-pity", "sadness","anguish",]
no_of_tweets = 1000000

columns = ["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet", "location"]
tweets_df = pd.DataFrame([], columns=columns)

for i in search_query:
    try:
        #The number of tweets we want to retrieve from the search
        tweets = api.search_tweets(q=i, count=no_of_tweets)

        #Pulling Some attributes from the tweet
        attributes_container = [[tweet.user.name, tweet.created_at, tweet.favorite_count, tweet.source,  tweet.text, tweet.user.location] for tweet in tweets]


        tweets_df = pd.concat([tweets_df, pd.DataFrame(attributes_container, columns=columns)], ignore_index=True)

    except BaseException as e:
        print('Status Failed On,',str(e))

tweets_df

tweets_df.to_csv("Data_Tweet.csv")



# Due to privacy concerns, the API keys have been removed. 
# If you're using this code, insert your own API keys in the appropriate places.

 consumer_key = "YOUR_CONSUMER_KEY"
 consumer_secret = "YOUR_CONSUMER_SECRET"
 access_key= "YOUR_ACCESS_KEY"
 access_secret = "YOUR_ACCESS_SECRET"


#Passing in  twitter API authentication key
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    access_key, access_secret
)

#the tweepy API
api = tweepy.API(auth, wait_on_rate_limit=True)


search_query = ["i'm Happy", "Excited", "feeling relaxed", "joy","gratitude"]
no_of_tweets = 1000000

columns = ["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet", "Place"]
undepress_tweets_df  = pd.DataFrame([], columns=columns)

for i in search_query:
    try:
        #The number of tweets we want to retrieve from the search
        tweets = api.search_tweets(q=i, count=no_of_tweets)

        #Pulling Some attributes from the tweet
        attributes_container = [[tweet.user.name, tweet.created_at, tweet.favorite_count, tweet.source,  tweet.text, tweet.user.location] for tweet in tweets]


        undepress_tweets_df = pd.concat([tweets_df, pd.DataFrame(attributes_container, columns=columns)], ignore_index=True)

    except BaseException as e:
        print('Status Failed On,',str(e))


undepress_tweets_df

undepress_tweets_df.to_csv("Data_Tweet_undepress.csv")





# Due to privacy concerns, the API keys have been removed. 
# If you're using this code, insert your own API keys in the appropriate places.

 consumer_key = "YOUR_CONSUMER_KEY"
 consumer_secret = "YOUR_CONSUMER_SECRET"
 access_key= "YOUR_ACCESS_KEY"
 access_secret = "YOUR_ACCESS_SECRET"


#Passing in  twitter API authentication key
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    access_key, access_secret
)

#the tweepy API
api = tweepy.API(auth, wait_on_rate_limit=True)


search_query = ["i'm Happy", "Excited", "feeling relaxed","healthy", "good health","love", "joy","gratitude"]
no_of_tweets = 1000000

columns = ["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet", "Place"]
undepress_tweets_df  = pd.DataFrame([], columns=columns)

for i in search_query:
    try:
        #The number of tweets we want to retrieve from the search
        tweets = api.search_tweets(q=i, count=no_of_tweets)

        #Pulling Some attributes from the tweet
        attributes_container = [[tweet.user.name, tweet.created_at, tweet.favorite_count, tweet.source,  tweet.text, tweet.user.location] for tweet in tweets]


        undepress_tweets0 = pd.concat([tweets_df, pd.DataFrame(attributes_container, columns=columns)], ignore_index=True)

    except BaseException as e:
        print('Status Failed On,',str(e))

undepress_tweets0

undepress_tweets0.to_csv("undepress_tweets0.csv")


# Due to privacy concerns, the API keys have been removed. 
# If you're using this code, insert your own API keys in the appropriate places.

 consumer_key = "YOUR_CONSUMER_KEY"
 consumer_secret = "YOUR_CONSUMER_SECRET"
 access_key= "YOUR_ACCESS_KEY"
 access_secret = "YOUR_ACCESS_SECRET"


#Passing in  twitter API authentication key
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    access_key, access_secret
)

#the tweepy API
api = tweepy.API(auth, wait_on_rate_limit=True)


search_query = ["i'm Happy", "Excited", "feeling relaxed", "joy","gratitude"]
no_of_tweets = 1000000

columns = ["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet", "Place"]
undepress_tweets_df  = pd.DataFrame([], columns=columns)

for i in search_query:
    try:
        #The number of tweets we want to retrieve from the search
        tweets = api.search_tweets(q=i, count=no_of_tweets)

        #Pulling Some attributes from the tweet
        attributes_container = [[tweet.user.name, tweet.created_at, tweet.favorite_count, tweet.source,  tweet.text, tweet.user.location] for tweet in tweets]


        undepress_tweets_df1 = pd.concat([tweets_df, pd.DataFrame(attributes_container, columns=columns)], ignore_index=True)

    except BaseException as e:
        print('Status Failed On,',str(e))

undepress_tweets_df1

undepress_tweets_df1.to_csv("Data_Tweet.csv")



import tweepy
import pandas as pd

# Due to privacy concerns, the API keys have been removed. 
# If you're using this code, insert your own API keys in the appropriate places.

 consumer_key = "YOUR_CONSUMER_KEY"
 consumer_secret = "YOUR_CONSUMER_SECRET"
 access_key= "YOUR_ACCESS_KEY"
 access_secret = "YOUR_ACCESS_SECRET"


#Passing in  twitter API authentication key
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    access_key, access_secret
)

#the tweepy API
api = tweepy.API(auth, wait_on_rate_limit=True)


search_query = ["i'm depressed", "loneliness", "feeling sad", "Suicidal thoughts", "feel angry", "lonely", "Suicidal","want to die", "self-pity", "sadness","anguish","mental health"]
no_of_tweets = 1000000

columns = ["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet", "location"]
tweets_df = pd.DataFrame([], columns=columns)

for i in search_query:
    try:
        #The number of tweets we want to retrieve from the search
        tweets = api.search_tweets(q=i, count=no_of_tweets)

        #Pulling Some attributes from the tweet
        attributes_container = [[tweet.user.name, tweet.created_at, tweet.favorite_count, tweet.source,  tweet.text, tweet.user.location] for tweet in tweets]


        twets_df = pd.concat([tweets_df, pd.DataFrame(attributes_container, columns=columns)], ignore_index=True)

    except BaseException as e:
        print('Status Failed On,',str(e))
        
twets_df

twets_df.to_csv('twet_df.csv')

tweets_data = pd.read_csv("/content/Comb-Data_Tweet.csv")
tweets_data

DF_1 = pd.read_csv("/content/main_comb.csv")
DF_1

tweets_data_N = pd.read_csv("/content/main_data.csv")
tweets_data_N

mental_df = pd.concat([ tweets_df,tweets_data,undepress_tweets_df,undepress_tweets0,undepress_tweets_df1,tweets_data_N,twets_df])

mental_df
mental_df.to_csv("Tweet_comb.csv")
