# Let's just use the local mongod instance. Edit as needed.

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST= 'mongodb'
MONGO_PORT = 27017
MONGO_DBNAME='dbtest'

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH) and deletes of individual items
# (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

# We enable standard client cache directives for all resources exposed by the
# API. We can always override these global settings later.
CACHE_CONTROL = 'max-age=200'
CACHE_EXPIRES = 200

# Our API will expose two resources (MongoDB collections): 'people' and works

import json

jsonstring=open("my_schema.json").read()


response =json.loads(jsonstring)


DOMAIN = {
    'response': response,
   # 'works': works,
}
