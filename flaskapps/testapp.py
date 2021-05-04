from flask import Flask

app=Flask(__name__)

@app.route('/test')
def hello_world():
    return '<h1> Hello This response is from Flask based application </h1>'


app.run()
