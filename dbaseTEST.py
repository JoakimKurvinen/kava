
from pymongo import MongoClient
import datetime
import pprint

client = MongoClient()
db = client.pymongo_test

posts = db.posts
#post_data = {
#	'temperature': 22,
#	'date': datetime.datetime.utcnow()
}#
#result = posts.insert_one(post_data)
#print('One post: {0}'.format(result.inserted_id))
#db.collection_names(include_system_collections=False)

#pprint.pprint(posts.find_one())


