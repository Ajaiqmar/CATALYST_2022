from flask import Flask,render_template,url_for
import twint
import os.path
import os,shutil

app = Flask(__name__)

@app.route("/")
def getRoot():
    if(os.path.isdir("E:\HACKATHON\CATALYST\DATA\zoho.csv")):
        os.remove("E:\HACKATHON\CATALYST\DATA\zoho.csv")

    config = twint.Config()
    config.Search = "zoho issues"
    config.Lang = "en"
    config.Limit = 100
    config.Store_csv = True
    config.Output = "DATA/zoho.csv"

    twint.run.Search(config)

    return {"status" : 200}

app.run(debug=True)
