#!/usr/bin/env python
"""
This module is for simple tweeting and can be imported for use in other files
"""

import tweepy

class API_Handler(object):

  config = {
    "consumer_key"        : "value",
    "consumer_secret"     : "value",
    "access_token"        : "value",
    "access_token_secret" : "value",
    }

  def __init__(self,config={}):
    if config:
      self.config = config
    else:
      self.config = API_Handler.config

  def get_api(self,cfg):
    self.auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    self.auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(self.auth)

  def tweet(self, tweet):
    # Fill in the values noted in previous step here

    self.api = self.get_api(self.config)

    self.tweet = tweet
  
    self.status = self.api.update_status(status=self.tweet)

if __name__ == "__main__":
  tweeter = API_Handler()
  tweeter.tweet('Test')
