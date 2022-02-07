from flask import Flask, request
import requests
import json
from parseUpdate import *




app = Flask(__name__)

@app.route("<secretPath>", methods=["POST"]) # Accepting Post Request in a secret path

def process_json():

    content_type = request.headers.get("Content-Type")

    if (content_type == "application/json"):

        update = request.json

        parseUpdate(update)

        return "OK"

    else :

        return "Invalid Request"




if __name__ == "__main__":

    app.run()
