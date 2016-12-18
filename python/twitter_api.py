#!/usr/bin/env python2
##https://blog.twitter.com/developer

import tweepy
from subprocess import Popen, PIPE


def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = {
    "consumer_key"        : "value",
    "consumer_secret"     : "value",
    "access_token"        : "value",
    "access_token_secret" : "value"
    }

  api = get_api(cfg)

## system info ##
  uptime = "/usr/bin/uptime"

  p = Popen([uptime, '-p'],stdout=PIPE)
  for x in p.stdout:
     mas = list(x)
     mas1=''.join(mas)
  tweet = "Your PI system uptime is {} ".format(mas1)
  
  status = api.update_status(status=tweet)
  #print(tweet)
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
