from eve import Eve


my_settings = {
    'MONGO_HOST': 'mongodb',
    'MONGO_PORT': 27017,
    'MONGO_DBNAME': 'the_db_name2',
    'DOMAIN': {'people': {}},
    'RESOURCE_METHODS' :['GET', 'POST', 'DELETE']
}

app = Eve(settings=my_settings)
app.run(debug=True)
