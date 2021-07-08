import requests
import json
import re

# Get the addresses for a postcode
#TODO: Make into function after

test_postcodes = ["E5 8TE", "E5 8TE", "E8 2LN", "E8 1HH", "E8 2HH"]

def get_addresses_for_postcode(postcode):

    auth_token = input("Please enter your authorisation token")

    # Check postcode string is valid
    pattern = re.compile("[A-Za-z][1-9] [1-9][A-Za-z]{2}")
    match = pattern.match(postcode)

    # Verify valid postcode
    if match != None:
        print("Invalid postcode.\nPostcode must have a space e.g. E8 5ER")
        return

    base_url = f"https://6kb2p9kgb0.execute-api.eu-west-2.amazonaws.com/production/api/v1/addresses/?postcode={postcode}"

    headers = {
        "Authorization" : auth_token
    }

    response = requests.get(base_url, headers=headers)

    response = response.json()

    return response

for postcode in test_postcodes:
    get_addresses_for_postcode(postcode)

