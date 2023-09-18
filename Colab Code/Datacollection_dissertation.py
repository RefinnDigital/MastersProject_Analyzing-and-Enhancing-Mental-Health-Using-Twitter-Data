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



import tweepy
import pandas as pd



consumer_key = "IgXYxlulbwYMKS6t0HJP128mQ"
consumer_secret = "MLnhrcylwasHvX8wytmxw49sN4ZEQvKbmocH9vgCe40HoOvjuS"
access_key= "1509839153982316546-scDA0A3JnXD7rU0PNtSJig6wBGgbRd"
access_secret = "FvPXJdbV6gKgfib7rfVZtolWhf2Z4QrACkxNRZpIWZPeK"

#Passing in  twitter API authentication key
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

data_1 =  pd.read_excel("/content/MH_tweets_1.xlsx")
data_1

data

data.to_csv("COMBINED_DF.csv")

DF = pd.read_csv("/content/Comb-Data_Tweet.csv")
DF

DF_1 = pd.read_csv("/content/main_comb.csv")
DF_1

DF_2 = pd.read_csv("/content/main_data.csv")
DF_2

data.to_csv("Tweet_comb.csv")

data.info()



tweets_df

#tweets_df.to_csv("Data_Tweet.csv")

tweets_data

#tweets_data.to_csv("Data_Tweet.csv")

consumer_key = "h1r2JohHCOMzrpZLXVZRRazi3"
consumer_secret = "HeTtOasCAxTxw78PikObFIYkPzuB21mBCgx5GUm1Stvz5MDfuW"
access_key= "964035289617494018-GKBW2kmouEOvBheRVLUd7x68MqNPlKU"
access_secret = "L9wiUBXQwbmP3HJlDQuHiw8lVomkU2KdtmQwhHaXgsgJh"

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

#undepress_tweets_df.to_csv("Data_Tweet_undepress.csv")

undepress_tweets_df



consumer_key = "SraD2oZY8D8MjpFJDHz6cIqe6"
consumer_secret = "cRKx6zfitVD1BMInCdB7YTczd30zxh7hiToQsea94UIBs4rh4D"
access_key= "1509839153982316546-PQnYJCu0Z6eodG2myvuiIoQPvg3ARD"
access_secret = "rNSaoPTNe0nQBePdsTkion4RrJdZHzJrS9NWesaqgdYZm"

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

#undepress_tweets0.to_csv("undepress_tweets0.csv")

consumer_key = "h1r2JohHCOMzrpZLXVZRRazi3"
consumer_secret = "HeTtOasCAxTxw78PikObFIYkPzuB21mBCgx5GUm1Stvz5MDfuW"
access_key= "964035289617494018-GKBW2kmouEOvBheRVLUd7x68MqNPlKU"
access_secret = "L9wiUBXQwbmP3HJlDQuHiw8lVomkU2KdtmQwhHaXgsgJh"

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

tweets_data_N

import tweepy
import pandas as pd

consumer_key = "h1r2JohHCOMzrpZLXVZRRazi3"
consumer_secret = "HeTtOasCAxTxw78PikObFIYkPzuB21mBCgx5GUm1Stvz5MDfuW"
access_key= "964035289617494018-GKBW2kmouEOvBheRVLUd7x68MqNPlKU"
access_secret = "L9wiUBXQwbmP3HJlDQuHiw8lVomkU2KdtmQwhHaXgsgJh"

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

#twets_df.to_csv('twet_df.csv')

twets_df

mental_df = pd.concat([ tweets_df,tweets_data,undepress_tweets_df,undepress_tweets0,undepress_tweets_df1,tweets_data_N,twets_df])

mental_df