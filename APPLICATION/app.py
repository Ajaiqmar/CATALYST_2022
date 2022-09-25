import twint
import os.path
import os,shutil,time,requests
import pandas as pd


class App:
    def __init__(self):

        while(True):
            self.analyseTheTweetsAndReport()
            time.sleep(86400)
            self.scrapeTheTweets()

    def scrapeTheTweets(self):
        if(os.path.isdir("E:\HACKATHON\CATALYST\DATA\zoho.csv")):
            os.remove("E:\HACKATHON\CATALYST\DATA\zoho.csv")

        config = twint.Config()
        config.Search = "zoho issues"
        config.Lang = "en"
        config.Limit = 100
        config.Store_csv = True
        config.Output = "DATA/zoho.csv"

        twint.run.Search(config)

    def analyseTheTweetsAndReport(self):
        df = pd.read_csv("DATA/zoho.csv",usecols=["username","tweet"])

        for ind,row in df.iterrows():
            url = "http://localhost:3000/server/customer_support_app_function/analyzeSentiment?tweet="+row["tweet"]

            resp = requests.post(url)
            print(resp.status_code)
            if(resp.status_code == 200):

                resp = resp.json();
                print(resp[0]["sentiment_prediction"][0]["document_sentiment"])
                if(resp[0]["sentiment_prediction"][0]["document_sentiment"] == "Negative"):

                    url = "http://localhost:3000/server/customer_support_app_function/reportOperator?username="+row["username"]+"&tweet="+row["tweet"]

                    resp = requests.post(url).json()

            time.sleep(30)


App()
