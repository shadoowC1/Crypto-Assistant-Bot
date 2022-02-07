import requests

import json

def getFeyData(data_command) :

    try :

        response = requests.get("https://feyorra.com/data/statistics")

        fey_data = response.json()

    except :

        data = "There was an error retrieving data , please try later"

        return data

    if data_command == "/price" or data_command == "/price@FeyorraBot" :

        usd_price = fey_data["usd_price"]

        data = usd_price + " $."

        return data

    elif data_command == "/total_supply" or data_command == "/total_supply@FeyorraBot" :

        total_supply = fey_data["total_supply"]

        data = total_supply + " Fey."

        return data

    elif data_command == "/circulating_supply" or data_command == "/circulating_supply@FeyorraBot" :

        circulating_supply = fey_data["circulating_supply"]

        data = circulating_supply + " Fey."

        return data

    elif data_command == "/apy" or data_command == "/apy@FeyorraBot" :

        apy = fey_data["apy"]

        data = apy + "%."

        return data

    elif data_command == "/total_staked_amount" or data_command == "/total_staked_amount@FeyorraBot" :

        total_staked_amount = fey_data["total_staked_amount"]

        data = total_staked_amount + " Fey."

        return data

    elif data_command == "/total_stakers" or data_command == "/total_stakers@FeyorraBot" :

        total_stakers = fey_data["total_stakers"]

        data = total_stakers + "."

        return data
