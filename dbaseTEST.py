
from pymongo import MongoClient
import datetime
import pprint
import subprocess

client = MongoClient()
db = client.pymongo_test

posts = db.posts
post_data = {
	'date': datetime.datetime.now(),
	'temperature': 29
}
result = posts.insert_one(post_data)
#print('One post: {0}'.format(result.inserted_id))
#db.collection_names(include_system_collections=False)

#pprint.pprint(posts.find_one( {'date': datetime.datetime.now() })  )

pprint.pprint( posts.find_one( {'temperature': 29}) )

subprocess.call(["mongoexport","--db", "db", "-c", "--posts", "--jsonArray", "--out", "temp_test.json"])


