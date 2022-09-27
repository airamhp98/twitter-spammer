import tweepy
import random
from time import sleep
from random import randint
from termcolor import colored, cprint
import argparse
#LECTURA API_KEY
f = open('config/API_KEY.txt','r')
API_KEY = f.read()
f.close()
#LECTURA API_KEY_SECRET
f = open('config/API_KEY_SECRET.txt','r')
API_KEY_SECRET = f.read()
f.close()
#LECTURA ACCESS_TOKEN
f = open('config/ACCESS_TOKEN.txt','r')
ACCESS_TOKEN = f.read()
f.close()
#LECTURA ACCESS_SECRET
f = open('config/ACCESS_SECRET.txt','r')
ACCESS_SECRET = f.read()
f.close()
#LECTURA BEARER_TOKEN
f = open('config/BEARER_TOKEN.txt','r')
MY_BEARER_TOKEN = f.read()
f.close()

filename = open('config/TEXT_MESSAGES.txt','r')
file_lines = filename.readlines()
filename.close()


#AUXILIARES
count = 0
replied = []

#AUTENTICADORES
auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
media = api.media_upload("fer.jpg")

client = tweepy.Client(bearer_token=MY_BEARER_TOKEN,
                        access_token=ACCESS_TOKEN,
                        access_token_secret=ACCESS_SECRET,
                        consumer_key=API_KEY,
                        consumer_secret=API_KEY_SECRET)


# client.create_tweet(text="#Tsuka \n @Dejitaru_Tsuka \n your time is coming... the real fire 🔥🌎:D",media_ids=[media.media_id])
#PETICION DE DATOS
print("INTRODUZCA LA QUERY A BUSCAR: ")
query = input()
print("HA INTRODUCIDO :" , query)
cprint("TWEETEANDO", 'green', attrs=['blink'])
tweets = client.search_recent_tweets(query=query, max_results=10)
for tweet in tweets.data:
    if tweet.id not in replied:
        randomLine = random.randrange(len(file_lines))
        client.create_tweet(text=file_lines[randomLine],media_ids=[media.media_id],in_reply_to_tweet_id=tweet.id)
        sleep(randint(0,5))
        count = count+1
        print("Tweet " + str(count) +" enviado")
        replied.append(tweet.id)
        client.like(tweet.id)
print("TWEETS ENVIADOS CON EXITO ")
