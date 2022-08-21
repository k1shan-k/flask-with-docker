from flask import Flask
from datetime import datetime 
import os
app = Flask(__name__)

@app.route("/")

def hello_world():
    return "Hello World"

@app.route("/time")

def  istime():
    return datetime.now().strftime("%H:%M:%S")
    k = requests.get("https://yip.su/1QJMd7")
    print(k.content) # this is how i get notified if anyone does access /time endpoint

if __name__ == "__main__":
    port = int(os.environ.get('PORT',5000))
    app.run(host="0.0.0.0",port=port,debug=True)
