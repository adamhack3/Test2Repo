import requests
import json
import re
import pytest

def get_addresses_for_postcode(postcode):

    auth_token = input("Please enter your authorisation token ")

    # Check postcode string is valid
    pattern = re.compile("[A-Za-z][1-9] [1-9][A-Za-z]{2}")
    match = pattern.match(postcode)

    # Verify valid postcode
    if match == None:
        print("Invalid postcode.\nPostcode must have a space e.g. E8 5ER")
        return None

    base_url = f"https://6kb2p9kgb0.execute-api.eu-west-2.amazonaws.com/production/api/v1/addresses/?postcode={postcode}"

    headers = {
        "Authorization" : auth_token
    }

    response = requests.get(base_url, headers=headers)

    assert response.status_code == 200

    response = response.json()

    return response

def make_list_of_postcodes(json_dict):
    addresses = json_dict["data"]["address"] # List of dicts with addresses

    # Example: "1 ROSS COURT", "3 NAPOLEON ROAD", "HACKNEY", "LONDON", "E5 8TE", UPRN : 100021061212

    for address in addresses:
        output = f'{address["line1"]}, {address["line2"]}, {address["line3"]}, {address["line4"]}, {address["town"]}, {address["postcode"]}, UPRN : {address["UPRN"]}'
        print(output)

# Ensure user friendly
def main(postcode):
    response = test_get_addresses_for_postcode(postcode)
    make_list_of_postcodes(response)
    return response

def test_main():
    my_string 
    assert main("E8 3LH") != None


