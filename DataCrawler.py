#Import the necessary methods from tweepy library
#from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import re
import csv
import tweepy as twp
import datetime
import json
import pandas as pd
from datetime import date
# Enter Twitter API Keys

#access_token = "19877313-SqqVQ1Wye8YvoeVVVTjPx8bTv0aQjuzdo1XFiel5L"
#access_token_secret = "uT2v6Lb8ANN27eTYHe6ODE9sRyuYo0LvfpezyussqaPW5"
#consumer_key = "5FwTJ2nT3C2CVyHawykUm5Pca"
#consumer_secret = "LBMnlM7YDPnvWKk3JnVC8vkmXsawbVV2AyCl0vzFODQf6moWEb"

#access_token = "787524853066706944-MOjfg7X0mpDXDhOUqrK7jF5zxrtzXXY"
#access_token_secret = "Xg42Kd5s3zencDZGhRoxXcd8dXJ0D5vG3yqKd7LEoApLP"
#consumer_key = "stwiuXVzfENG9lkooJE9ACPpL"
#consumer_secret = "Aee96cubg77SsZSa2zCB890ajl6L4fADjxrh3F5LQqRmV9vzWr"

access_token ="787524853066706944-Bb37mCCJJATuzUYHA0V9L6ASNfUNEpy"
access_token_secret = "7Tev7UtgAXBTimXXhERuyTtLC2iw1W7gjuk2utkR9TmZX"
consumer_key = "awiu52XPkrebyRXo2PYheA9gi"
consumer_secret = "RIC2KBYED8sB8jkqPJt3BUfJXuD8F0av3hlWY8RvQj0ziE6PUw"



# Handle Twitter authetification and the connection to Twitter Streaming API
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api=twp.API(auth)

#hashtags=["#شاد","#شادی","#خوشحالی","#زیبایی","#زیبا","#حال_خوب","#عشق","#دوستی","#صفا","#صمیمیت","#صمیمی","#پیشرفت","#خنده","#مسرور","#مثبت","#خوش","#خوشرویی","#آغوش","#خوبی","#دوست_داشتن"]
hashtags=["#غم","#ناراحتی","#بدبختی","#بیشعور","#ناله","#بدی","#فحش","#دشنام","#گریه","#عزا","#بد","#بدحالی","#حال_بد","#سنگسار","#له_کردن","#تبعیض","#کشتار","#کشتن","#کتک_زدن","#توسریخور","#ظلم","#ظلم_و_ستد","#نادانی","#زشتی","#زشت","#دورویی","#دروغ","#دروغگویی","#پست_فطرت","#پستفطرت"]


endDate='2022-08-09'

df2=pd.DataFrame(columns=["Hashtag","ID","Date","Text"])
for hashtag in hashtags:
  tweets=twp.Cursor(api.search_tweets,q=hashtag,lang="fa",result_type="recent",include_entities=True, until=endDate,count=100).items(3500)
  for tw in tweets:
      df = pd.DataFrame({"Hashtag": [hashtag],
                         "ID": [tw.id_str],
                         "Date": [tw.created_at],
                         "Text": [tw.text]})
      df2=df2.append(df)
today = date.today()
d1 = today.strftime("%d%m%Y")
df2=df2.reset_index()
#with open('positiveSample'+d1+'.json', 'w', encoding='utf-8') as file:
with open('negativeSample'+d1+'.json', 'w', encoding='utf-8') as file:
    df2.to_json(file, force_ascii=False)      
