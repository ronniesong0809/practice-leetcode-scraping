import json
import requests
import os
from utils.runtime import runtime

@runtime
def getJsonFile():
    url = "https://leetcode.com/problems/api/tags/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "cookie": os.environ.get("LEETCODE_COOKIE")
    }
    r = requests.get(url=url, headers=headers)
    data = r.json()
    with open('data/problemsApiTags.json', 'w') as f:
        json.dump(data, f)

@runtime
def saveToFile():
    with open('data/problemsApiTags.json') as f:
        data = json.loads(f.read())
        topics = data["topics"]
        companies = data["companies"]
        dump(topics, "db/allTopics.json")
        dump(companies, "db/allCompanies.json")

def dump(data, output):
    with open(output, "w") as f:
        for x in data:
            list = []
            qlist = x['questions']
            qlist.sort()
            for y in qlist:
                list.append(str(y))

            x['questions'] = list
            x['count'] = len(list)
        json.dump(data, f)

@runtime
def run():
    getJsonFile()
    saveToFile()

def main():
    run()

if __name__ == "__main__":
    main()
