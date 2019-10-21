from eve import Eve

settings = {'DOMAIN': {'people': {}}}

app = Eve(settings=settings)

serve(app, host='0.0.0.0', port=8080)

app.run()
