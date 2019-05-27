from flask import Flask, render_template, redirect, request, url_for
from db import MongoDB, DBProxy, json

uri = "mongodb+srv://dbUser:dbPassword@hack-roles-rvxnw.mongodb.net/test?retryWrites=true&ssl_cert_reqs=CERT_NONE"

 
app = Flask(__name__)


db = MongoDB(uri)
# proxy_db = DBProxy("roles.json")


@app.route('/', methods = ["GET", "POST"])
def index():   
    processed_data = []
    for item in db["roles-info"].find():
        processed_data.append(item)

    for item in processed_data:
        item["qualifications"] = item["qualifications"][1:-1].split(",")
        item["prompt"] = item["prompt"][1:-1].split(",")

    # processed_data = proxy_db.items()

    return render_template("index.html", info_list = processed_data)
 
@app.route('/add', methods = ["GET", "POST"])
def add_entry(): 
    if request.method == "POST":
        db["roles-info"].insert_one(dict(request.form))
        # proxy_db.create(dict(request.form))
        return redirect(url_for("index"))

    return render_template("add_entry.html")

if __name__ == '__main__':  
    app.run(debug = True) 