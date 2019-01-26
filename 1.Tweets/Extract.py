import tweepy
from tweepy import OAuthHandler
import csv
import unicodedata

consumer_key = 'pEJDNax0fE1YVmWxF6MExyMux'
consumer_secret = 'w6sIoChAfIqm6MIvBr18TKZfVrUSJ1IGbEaF5wvHu4ql0CCE1O'
access_token = '962148968271699969-SxV2HaLSaVsax1g7upnDbag7u7Ue0Yl'
access_secret = 'wi6UFUbge7WKJsyCgf8a3MAn9x6ff1sq8AhQC5OpDSVA6'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

Lista_Timeline = ["LivCultura"]

for timeline in Lista_Timeline:
    print(timeline)
    csvFile = open('%s.csv' %timeline, 'a', encoding="utf-8")
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(["Data_Tweet", "Autor", "Local", "Tweet_Text", "Retweeted", "Favourited", "Retweet Count",
                        "Favorite Count", "In Reply to", "Reply Message"])
    for tweet in tweepy.Cursor(api.user_timeline, id=timeline, count=1, exclude_replies=False,tweet_mode="extended").items():
        if(tweet.in_reply_to_status_id == None):
            reply_text = ""
        else:
            try:
                reply_text = unicodedata.normalize('NFKD', api.get_status(tweet.in_reply_to_status_id,tweet_mode="extended").full_text).encode('ASCII', 'ignore').decode('ASCII')
            except:
                reply_text = ""

        csvWriter.writerow([tweet.created_at, tweet.author.name, tweet.geo,
                            unicodedata.normalize('NFKD', tweet.full_text).encode('ASCII', 'ignore'),
                            tweet.retweeted, tweet.favorited, tweet.retweet_count, tweet.favorite_count,
                            tweet.in_reply_to_screen_name,reply_text])
csvFile.close()



