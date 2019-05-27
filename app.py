from flask import Flask, render_template, redirect, request, url_for
from db import MongoDB, DBProxy, json

uri = "mongodb+srv://dbUser:dbPassword@hack-roles-rvxnw.mongodb.net/test?retryWrites=true&ssl_cert_reqs=CERT_NONE"

 
app = Flask(__name__)

# TO_DO(1): Choose which database to use
db = MongoDB(uri)
# proxy_db = DBProxy("roles.json")


@app.route('/', methods = ["GET", "POST"])
def index():   
    # TO_DO(2): Preprocess qualifications and prompt into lists 
    processed_data = []
    # TO-DO(3): ONLY FOR DB: Append data into list from find(), 
    #                        Go through each entry and slice ends off, split by ',', for qualifications and prompt fields

    # processed_data = proxy_db.items()

    # TO_DO(4): Render index with processed data and go into index.html and jinja2 template
    
 
@app.route('/add', methods = ["GET", "POST"])
def add_entry(): 
    # TO_DO(6): Once method is POST, insert into db new data (as a dict) and redirect url for index

    # TO-DO(7): Render template for add_entry.html
    
    pass

if __name__ == '__main__':  
    app.run(debug = True) 