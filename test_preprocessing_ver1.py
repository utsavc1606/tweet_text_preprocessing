import json
import re
import sys

input_file_path = 'C:\\Users\\Utsav Chatterjee\\Documents\\python_code\\collected_twitter_data\\'
input_data_file = 'stream_sprint_t-mobile_tmobile_verizon_att.json'

with open(input_file_path + input_data_file, 'r') as f:
    lines = f.readlines() # read tweets/lines

sys.stdout = open('preprocessing_output.txt', 'w')

keys_list = ["created_at",
             "id_str",
             "text",
             "source",
             "user",
             "geo",
             "coordinates",
             "place",
             "reply_count",
             "retweet_count",
             "favorite_count",
             "favorited",
             "retweeted",
             "filter_level"]

user_keys_list = ["id",
                 "name",
                 "screen_name",
                 "location",
                 "description",
                 "followers_count",
                 "friends_count",
                 "listed_count",
                 "favourites_count",
                 "statuses_count",
                 "created_at",
                 "time_zone",
                 "geo_enabled",
                 "lang"]

final_tweet_list = []

for l in lines:
    if len(l) > 1:
        tweet_list = []
        tweet = json.loads(l) # load it as Python dict
        for keys in keys_list:
            if keys != "user":
                tweet_list.append(str(tweet[keys]))
            else:
                for key in user_keys_list:
                    tweet_list.append(str(tweet[keys][key]))
        final_tweet_list.append("|".join(tweet_list))

print("b'created_at|id_str|text|source|id|name|screen_name|location|description|followers_count|friends_count|listed_count|favourites_count|statuses_count|created_at|time_zone|geo_enabled|lang|geo|coordinates|place|reply_count|retweet_count|favorite_count|favorited|retweeted|filter_level'")

for i in final_tweet_list:
    print(i.encode("ascii", "ignore"))

sys.stdout.close()

with open('preprocessing_output.txt', 'r') as g:
    lines = g.readlines()

# outfile = open("testfile.out", "w")
# for x in lines:
#     outfile.write(x.decode("utf-8"))
