import requests


def news_api():
    url = "https://api.apify.com/v2/key-value-stores/toDWvRj1JpTXiM8FF/records/LATEST?disableRedirect=true"

    headers = {
        'x-rapidapi-key': "a84ce2b994msh2cb21874567e1a1p1e6638jsn79381780c485",
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    return response

