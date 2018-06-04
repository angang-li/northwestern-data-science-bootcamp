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

# Scan for mentions
def scan(newest_tweet, api=api):

    """
    Scan for mentions
    input:
        newest_tweet - int, since_id used to filter the search
    output:
        target_account - str, target account name to pull tweets for sentiment analysis
        request - dict, dictionary of text, author, id, and time of the request
    """

    # Target Term
    my_account = "@alf7tf"
    search_term = f"{my_account} Analyze:"

    # Retrieve the most recent tweets
    public_tweets = api.search(search_term, count=10, result_type="recent", since_id=newest_tweet)

    if len(public_tweets['statuses']) > 0:

        # Retrieve tweet text, author, id, and time
        tweet = public_tweets['statuses'][-1]
        text = tweet['text']
        tweet_author = "@" + tweet["user"]["screen_name"]
        tweet_id = tweet['id']
        raw_time = tweet['created_at']
        datetime_time = datetime.datetime.strptime(raw_time, "%a %b %d %H:%M:%S %z %Y")
        request = {'text': text, 'author': tweet_author, 'id': tweet_id, 'time': datetime_time}
        
        # Identify account to analyze
        account_seperators = ':,;.!?'
        target_account = text.replace(search_term, "").strip(':,;.!?').strip()

        for seperator in account_seperators:
            if seperator in target_account:
                target_account = target_account.split(seperator)[0].strip()
        
    else:
        target_account = ''
        request = {}
        
    return target_account, request

# Pull 500 most recent tweets
def pull(target_account, api=api):
    
    """
    Pull 500 most recent tweets
    input:
        target_account - str, target account name to pull tweets for sentiment analysis
    output:
        tweets_data - list, list of the 500 tweets
    """
    
    # Create variable for holding the oldest tweet
    oldest_tweet = None
    tweets_data = []

    for x in range(5):
        
        # Get 100 tweets by the target user
        public_tweets = api.user_timeline(target_account, count=100, result_type="recent", max_id=oldest_tweet)
        tweets_data.extend(public_tweets)
        
        # Reassign the oldest tweet
        for tweet in public_tweets:
            tweet_id = tweet["id"]
            oldest_tweet = tweet_id - 1    
    
    return tweets_data

# Analyze sentiment
def analyze(tweets_data):

    """
    Analyze sentiment of tweets
    input:
        tweets_data - list, list of the 500 tweets
    output:
        df - DataFrame, dataframe that stores polarity score, tweet text, and # tweets ago
    """

    # Preallocate variables for analysis
    texts = []
    tweets_ago = []
    polarities = []
    counter = 0
    
    for tweet in tweets_data:
        
        # Retrieve tweet info
        text = tweet['text']
        
        # Run sentiment analysis
        testimonial = TextBlob(text)
        polarity = testimonial.sentiment.polarity

        # Store in list
        texts.append(text)
        tweets_ago.append(counter)
        polarities.append(polarity)
        
        counter -= 1
    
    # Write to dataframe
    df = pd.DataFrame({'text':texts, 'tweets ago':tweets_ago, 'polarity score':polarities})
    
    return df

# Plot sentiment over time
def plot(df, target_account):
    
    """
    Plot sentiment over time
    input:
        df - DataFrame, dataframe that stores polarity score, tweet text, and # tweets ago
        target_account - str, target account name to pull tweets for sentiment analysis
    output:
        fig_name - str, file name of the saved figure
    """
    
    mpl.rcParams['figure.dpi']= 100
    mpl.rcParams['font.family'] = 'sans-serif'
    mpl.rcParams['font.sans-serif'] = ['Arial']
    sns.set(color_codes=True)
    today_date = datetime.date.today().strftime("%m/%d/%y")

    # Plot
    plt.plot(df["tweets ago"], df["polarity score"], label = target_account, marker = 'o', markersize = 6,
                color='steelblue', linewidth=0.5)

    # Format the plot
    fig_name = f'polarity_images/polarity_{target_account}.png'
    plt.yticks(np.arange(-1,1.5,0.5))
    plt.xlim((df['tweets ago'].min()-10, 10))
    plt.ylim((-1.05, 1.05))
    plt.xlabel('Tweets Ago')
    plt.ylabel('Tweet Polarity')
    plt.title(f'Sentiment Analysis of Tweets ({today_date})')
    plt.legend(loc='upper left', frameon=False, title='Tweets Source', bbox_to_anchor=[1,1])
    plt.savefig(fig_name, bbox_inches="tight", dpi = 300)
    plt.close()
    None
    
    return fig_name

# Tweet out
def tweet_out(fig_name, target_account, request, api=api):
    
    """
    Create a twitter status update
    input:
        fig_name - str, file name of the saved figure
        target_account - str, target account name to pull tweets for sentiment analysis
        request - dict, dictionary of text, author, id, and time of the request
    output:
        status_output - status object
    """
    
    status = f"New Tweet Analysis: {target_account} (Thx {request['author']}!!)"
    status_output = api.update_with_media(filename = fig_name, status = status)

    return status_output