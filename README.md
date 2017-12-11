Add s.dwitter.com to /etc/hosts and point to IP address of search container

cat doc.json
{
    "fields": {
	 "user": "jobergum”
         "tweet": "Vespa meetup going down right no”,
         "hashtags": [“vespa.ai”],
          "timestamp": 1512084275
    }
}

POST IT 
curl -X POST --data-binary @doc.json http://s.dwitter.com:8080/document/v1/twitter/tweet/docid/1 -s |python -m json.tool


Simple GET
http://s.dwitter.com:8080/document/v1/twitter/tweet/docid/1

Start stream of updates. 

Need to install https://github.com/bear/python-twitter

sudo pip install python-twitter

python twitter-api-get-sample.py | vespa-feeder -v 


Query Examples 

Weightedset query: 
http://s.dwitter.com:8080/search/?yql=select%20*%20from%20sources%20*%20where%20weightedSet(user,%20%7B%22divaradiodisco%22:1,%20%22Wally_Callahan%22:1%7D)%3B

Regular expression:
http://s.dwitter.com:8080/search/?yql=select%20*%20from%20sources%20*%20where%20hashtags%20contains%20%22trump%22%3B&select=all(group(fixedwidth(timestamp,60))%20order(-max(timestamp))each(output(count())))&hits=0

Range search:
http://s.dwitter.com:8080/search/?yql=select%20*%20from%20sources%20*%20where%20range(timestamp,1512408240,1512408300)%3B&

Grouping examples

http://s.dwitter.com:8080/search/?yql=select%20*%20from%20sources%20*%20where%20hashtags%20matches%20%22%5Etrum%22%3B&select=all(group(hashtags)%20max(10)%20order(-count())%20each(output(count())))&hits=0

http://s.dwitter.com:8080/search/?yql=select%20*%20from%20sources%20*%20where%20hashtags%20contains%20%22trump%22%3B&select=all(group(fixedwidth(timestamp,60))%20order(-max(timestamp))each(output(count())))&hits=0

http://s.dwitter.com:8080/search/?yql=select%20*%20from%20sources%20*%20where%20hashtags%20contains%20%22trump%22%3B&select=all(group(hashtags)%20max(10)%20order(-count())%20each(output(count())%20max(2)%20each(output(summary()))))
