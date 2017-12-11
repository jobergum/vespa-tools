import twitter,time,calendar,json,unicodedata

def remove_control_characters(s):
    return "".join(ch for ch in s if unicodedata.category(ch)[0]!="C")

api = twitter.Api(consumer_key='xx',
                      consumer_secret='xx',
                      access_token_key='xx',
                      access_token_secret='xx'

api.VerifyCredentials()

#replace with topics of interest
sample = api.GetStreamFilter(track=["donald","trump"])

print "["
for s in sample:
	if s.has_key("text"):
		text = s["text"]
		text = remove_control_characters(text)
		#text = text.encode('utf-8')
		id = s["id"]
		hashtags = []
		if s.has_key("entities"):
			hashtags = s["entities"]["hashtags"]
			tags = []
			for tag in hashtags:
				t = tag["text"]
				t = remove_control_characters(t)
				#t = t.encode('utf-8')
				tags.append(t)
			hashtags = tags
		ts = time.strptime(s['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
		in_reply_to_screen_name = s["in_reply_to_screen_name"]
		user_name = s['user']['screen_name']
		if not text.startswith("RT") and in_reply_to_screen_name is None:

			print json.dumps({"put":"id:twitter:tweet::%s" %(id),
				"fields":{"text":text,"hashtags":hashtags,"timestamp":calendar.timegm(ts),"user":user_name}})
		 	print ","
print "]"	
