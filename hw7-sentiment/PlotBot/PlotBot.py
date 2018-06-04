# Twitter sentiment plot bot

##############
# Dependencies
import json
import tweepy
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
import seaborn as sns
import datetime
import time

# Import Twitter API Keys
from config import consumer_key, consumer_secret, access_token, access_token_secret

# Import and Initialize Sentiment Analyzer
from textblob import TextBlob

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Import functions
from PlotBot_functions import scan, pull, analyze, plot, tweet_out

##############
# Execute PlotBot
# Analyzed account names
account_analyzed = []
counter = 0
newest_tweet = None

while counter < 10:
    
    # Scan for mention
    target_account, request = scan(newest_tweet)
    
    # If the target account is not empty and if the target account has not been analyzed
    if (len(target_account.strip('@')) > 0) & (target_account.lower() not in account_analyzed):
        
        # Reassign to only include tweets newer than the previous
        newest_tweet = request['id'] + 1

        # Append to the list of analyzed account names
        account_analyzed.append(target_account.lower())
            
        try: 
            
            # Pull tweets
            tweets_data = pull(target_account)
            
            # Analyze sentiment
            df = analyze(tweets_data)
            
            # Plot sentiment
            fig_name = plot(df, target_account)
            
            # Tweet out
            status_output = tweet_out(fig_name, target_account, request)

            # Successful execution
            counter += 1
            print(f"\nRequest #{counter}: {target_account} analysis completed.")
            print(f"{request['time']}")

        except:
            print(f"\nRequested account {target_account} does not exist.")
    
    else:
        print("\nNo new request.")

    # Wait 5 minutes before another scan
    time.sleep(5*60)
