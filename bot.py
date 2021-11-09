import pandas as pd
import numpy as np
from secrets import *
import tweepy
from flask import Flask
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import time

def get_from_csv():
	'''
		@TODO
			- read file from github page
	'''
	df = pd.read_csv("input.csv",sep=';',usecols= ['user','comida'])
	matrix = df.apply(lambda x: x.dropna().tolist()).tolist()
	
	return (np.random.choice(matrix[0]), np.random.choice(matrix[1]))

def create_tweet():
	user, comida = get_from_csv()
	print(user,comida)
	tweet = """
            Já convidou o @{} para comer um ~{} no @TeComoEmCasa hoje?
            """.format(user, comida)
	return tweet
	
def tweet_send():
	intervalo = 60 * 60 * 24 #roda a cada 24h
	auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
	auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
	api = tweepy.API(auth)
	
	while True:
		print("tweetandoo...")
		tweet_txt = create_tweet()
		api.update_status(tweet_txt)
		time.sleep(intervalo)

if __name__ == "__main__" :
	tweet_send()