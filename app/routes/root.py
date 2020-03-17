from flask import current_app as app

@app.route('/')
def helloworld():
    return "Hello World!"
