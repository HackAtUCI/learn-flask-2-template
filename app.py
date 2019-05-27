from flask import Flask, render_template, redirect, request, url_for
from db import MongoDB, DBProxy

uri = "mongodb+srv://dbUser:dbPassword@hack-roles-rvxnw.mongodb.net/test?retryWrites=true&ssl_cert_reqs=CERT_NONE"

# https://cloud.mongodb.com/v2/5cc7e3fdc56c98c27c6a7fc8#clusters/detail/hack-roles
 
app = Flask(__name__)
db = MongoDB(uri)
proxy_db = DBProxy("roles.json")


@app.route('/', methods = ["GET", "POST"])
def index():   
        return render_template("index.html", info_list = db["roles-info"].find())
        #return render_template("index.html", info_list = proxy_db.items())

@app.route('/add', methods = ["GET", "POST"])
def add_entry(): 
        if request.method == "POST":
            db["roles-info"].insert_one(dict(request.form))
            #proxy_db.create(dict(request.form))
            return redirect(url_for("index"))
 
        return render_template("add_entry.html")

if __name__ == '__main__':  
    app.run(debug = True) 