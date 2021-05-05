import requests


def news_api():
    url = "https://api.apify.com/v2/key-value-stores/toDWvRj1JpTXiM8FF/records/LATEST?disableRedirect=true"

    headers = {
        'x-rapidapi-key': "a84ce2b994msh2cb21874567e1a1p1e6638jsn79381780c485",
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    return response


news_api()

data = [
    {
        "id": "2bf95f59-96bc-4904-b430-284f36b90063",
        "symbol": "IND",
        "Country": "India",
        "Continent": "Asia",
        "date": "2021-05-02",
        "total_cases": 19925517,
        "new_cases": 368060,
        "total_deaths": 218959,
        "new_deaths": 3417,
        "total_tests": 0,
        "new_tests": 0
    },
    {
        "id": "ce5589c4-436c-41df-a632-ab9e01a5f83f",
        "symbol": "IND",
        "Country": "India",
        "Continent": "Asia",
        "date": "2021-05-01",
        "total_cases": 19557457,
        "new_cases": 392488,
        "total_deaths": 215542,
        "new_deaths": 3689,
        "total_tests": 0,
        "new_tests": 0
    },
    {
        "id": "6981b70a-7d12-4730-b2e1-96f2ef45fc6c",
        "symbol": "IND",
        "Country": "India",
        "Continent": "Asia",
        "date": "2021-04-27",
        "total_cases": 17997113,
        "new_cases": 360927,
        "total_deaths": 201187,
        "new_deaths": 3293,
        "total_tests": 280979877,
        "new_tests": 1658700
    },
    {
        "id": "b809f7dd-7cbc-47b5-a840-cb2f3fea2194",
        "symbol": "IND",
        "Country": "India",
        "Continent": "Asia",
        "date": "2021-04-25",
        "total_cases": 17313163,
        "new_cases": 352991,
        "total_deaths": 195123,
        "new_deaths": 2812,
        "total_tests": 0,
        "new_tests": 0
    },
    {
        "id": "2a23f43b-c17d-440e-a3ed-f3d9afd17bc4",
        "symbol": "IND",
        "Country": "India",
        "Continent": "Asia",
        "date": "2021-04-23",
        "total_cases": 16610481,
        "new_cases": 346786,
        "total_deaths": 189544,
        "new_deaths": 2624,
        "total_tests": 274445653,
        "new_tests": 1740550
    },
    {
        "id": "769ea32b-c331-44c7-95eb-426d062da325",
        "symbol": "IND",
        "Country": "India",
        "Continent": "Asia",
        "date": "2021-04-18",
        "total_cases": 15061805,
        "new_cases": 273802,
        "total_deaths": 178769,
        "new_deaths": 1619,
        "total_tests": 0,
        "new_tests": 0
    },
    {
        "id": "cc670eec-5808-4286-941f-ac56fd284a3b",
        "symbol": "IND",
        "Country": "India",
        "Continent": "Asia",
        "date": "2021-04-17",
        "total_cases": 15061805,
        "new_cases": 261394,
        "total_deaths": 177150,
        "new_deaths": 1501,
        "total_tests": 0,
        "new_tests": 0
    }
]
context = {}
for i in data:
    context.update({
        'Country': i['Country'], 'date': i['date'], 'total_tests': i['total_tests'],
        'new_cases': i['new_cases'], 'new_deaths': i['new_deaths'], 'new_tests': i['new_tests'],
    })

print(context)
