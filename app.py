from flask import (
    Flask, request, jsonify, session, url_for, redirect,
    render_template, flash, send_file, send_from_directory
)
import os
from pymongo import MongoClient
import json
app = Flask(__name__)
app.secret_key = os.urandom(24)

from pymongo import MongoClient
import certifi

MONGO_URI = "mongodb+srv://umeshyenugula2007_db_user:fwmIOPGPWBnzIoce@agritrade.29grdah.mongodb.net/Feedback?retryWrites=true&w=majority&appName=ideaquest"

try:
    client = MongoClient(
        MONGO_URI,
        tls=True,
        tlsCAFile=certifi.where(),   
        serverSelectionTimeoutMS=10000
    )
    client.admin.command('ping')
    print("✅ MongoDB connection successful!")
except Exception as e:
    print("❌ MongoDB connection failed:", e)


MONGO_URI = "mongodb+srv://umeshyenugula2007_db_user:fwmIOPGPWBnzIoce@agritrade.29grdah.mongodb.net/"
client = MongoClient(MONGO_URI)
db = client["IdeaQuest"]
teams=db["Teams"]
feedback=db["Response"]
app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def home():
    if request.method=="POST":
        teams.insert_one({"teamcode":1})
        teamcode=request.form.get("teamcode",None)
        if teamcode==None or teamcode=="":
            return render_template("index.html")
        return render_template("feedback.html")
    return render_template("index.html")
app.run(debug=True)
