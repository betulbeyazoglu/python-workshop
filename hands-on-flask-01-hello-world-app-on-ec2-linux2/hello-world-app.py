from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
    return "Hello world"

if __name__=='__main__':
    #app.run('localhost', port=5000, debug=True) for run internally
    #app.run(debug=True) -->same with last one
    app.run('0.0.0.0', port=80) #for run on internet