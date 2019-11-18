MONGO_HOST= 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME='armundia1'

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

#import json

#jsonstring=open("my_schema.json").read()


#response =json.loads(jsonstring)


DOMAIN = {
    'response': {
        'schema': {
           'codAssetTest': {
            'type': 'string',
            'required': True,
    }},
   
         'allow_unknown': True,
          'item_lookup': True,
          'additional_lookup': {
          'url': 'regex("[\w]+")',
           'field': 'codAssetTest',
        } } 
   # 'works': works,
}
