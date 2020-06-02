import requests


def getSentiment(text):
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }

    data = '{ "text": [ "%s" ]}' % (text)

    response = requests.post(
        "http://localhost:5000/model/predict", headers=headers, data=data
    ).json()
    positive = response["predictions"][0]["positive"]
    negative = response["predictions"][0]["negative"]

    return (positive, negative)
