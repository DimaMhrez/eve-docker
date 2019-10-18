from eve import Eve

settings = {'DOMAIN': {'people': {}}}

app = Eve(settings=settings)
export Eve_ENV=developmen
app.run()
