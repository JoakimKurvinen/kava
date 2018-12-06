
from pymongo import MongoClient
import datetime
import pprint
import subprocess

client = MongoClient()
db = client.pymongo_test   # pymongo_test is the name of the dbase

posts = db.posts    # posts is the name of the Collection
#post_data = {
#	'date': datetime.datetime.now(),
#	'temperature': 29
#}
#result = posts.insert_one(post_data)

#post_data = [
#	{
#	'date': datetime.datetime.now(),
#	'temperature': 29},
#	{
#	'date': datetime.datetime.now(),
#	'temperature': 24},
#	{
#	'date': datetime.datetime.now(),
#	'temperature': 26}]
#	
#result = posts.insert_many(post_data)

#print('One post: {0}'.format(result.inserted_id))
#db.collection_names(include_system_collections=False)

#pprint.pprint(posts.find_one( {'date': datetime.datetime.now() })  )

#pprint.pprint( posts.find_one( {'temperature': 29}) )

#for post in posts.find():   #find all documents
#        pprint.pprint(post)

subprocess.call(["mongoexport","--db", "pymongo_test", "-c", "posts", "--jsonArray", "--out", "temp_test.json"])


