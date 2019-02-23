from flask import Flask

app=Flask(__name__)
@app.route("/")
def index():
    return "hello...."
@app.route("/home")
def home():
    return "My home page"
@app.route("/contact")
def contact():
    return "8547570769"
if(__name__=="__main__"):
    app.run()