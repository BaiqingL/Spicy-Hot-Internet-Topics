from getSentiment import getSentiment
import requests, re


def spiciestInSub(subreddit, posted):
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    r = requests.get(url, headers={"user-agent": "Mozilla/5.0"}).json()["data"][
        "children"
    ]
    spiciestPost = ""
    negativeSenti = 0
    item = {}
    limit = 0
    for items in r:
        if limit < 15:
            temp = items["data"]["title"]  # ["url"]
            if temp not in posted:
                temp = re.sub(r"[^A-Za-z0-9 ]+", "", temp)
                if items["data"]["num_comments"] > 20 and len(temp) > 50:
                    if spiciestPost == "":
                        spiciestPost = temp
                        negativeSenti = getSentiment(spiciestPost)[1]
                        item = items
                    else:
                        tempSenti = getSentiment(temp)[1]
                        if tempSenti > negativeSenti:
                            spiciestPost = temp
                            negativeSenti = tempSenti
                            item = items
                    print("Processed post:", temp, "from", subreddit)
                limit += 1
    return (item["data"]["title"], item["data"]["url"], negativeSenti)
