import json
import requests

def getJsonFile():
    url = "https://leetcode.com/problems/api/tags/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "cookie": "_ga=GA1.2.37052354.1606567733; __stripe_mid=8f3b50cb-b0df-4231-869f-056091828c2d36b551; csrftoken=NPIQLYahmRJrGm5gob0f9ZvUhColNdKs6ZFI76pEMJysFGG51y8eu8mk4Xzx4BbF; gr_user_id=66e7429a-be1e-46c8-b2dc-258ca871d86a; 87b5a3c3f1a55520_gr_last_sent_cs1=ronsong; __atuvc=0|22,0|23,4|24,0|25,4|26; NEW_PROBLEMLIST_PAGE=1; 87b5a3c3f1a55520_gr_cs1=ronsong; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMjExNzMzNyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImMwNzJmYzdkYjZjZmYyZDM2ZTk2YTg2MGUzY2VjODUwNGEyNmE2MzMiLCJpZCI6MjExNzMzNywiZW1haWwiOiJyb25zb25nQHBkeC5lZHUiLCJ1c2VybmFtZSI6InJvbnNvbmciLCJ1c2VyX3NsdWciOiJyb25zb25nIiwiYXZhdGFyIjoiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUuY29tL3VzZXJzL3JvbnNvbmcvYXZhdGFyXzE1OTkzMDg1NzYucG5nIiwicmVmcmVzaGVkX2F0IjoxNjI1OTA3MTk0LCJpcCI6IjczLjE4MC4xNy4yMTIiLCJpZGVudGl0eSI6IjM2NTFmMDcyMzk1MzQ3NTM3Yzc0MDg5OTg5Yzg4YTY2Iiwic2Vzc2lvbl9pZCI6ODcwMDM4NCwiX3Nlc3Npb25fZXhwaXJ5IjoxMjA5NjAwLCJjb252ZXJzaW9uX3RhcmdldHMiOnsiUnh0YVZ4RUtBUVJIR1VWUVNoZ1hGUU1VVEJRR0FCd0VEUXRCRkZkYlFGOGFIVkpRRmhzWEFnPT0iOnsic2VuZF9zZXNzaW9uX2lkcyI6WzE0NzJdLCJlbWFpbCI6InJvbnNvbmdAcGR4LmVkdSJ9LCJSeHRhVnhFS0FRUkhEMUJjRGdNTFhRc1hXMDBBSEFaZFdrd0hGZz09Ijp7InNlbmRfc2Vzc2lvbl9pZHMiOlsxNDcyXSwiZW1haWwiOiJyb25zb25nQHBkeC5lZHUifX19.UoGOwtJxQmfdYiQpy4h5jCYKUL4JyOj-XVQRU6ryqds"
    }
    r = requests.get(url=url, headers=headers)
    data = r.json()
    with open('data/problemsApiTags.json', 'w') as f:
        json.dump(data, f)

    
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

def main():
    getJsonFile()
    saveToFile()

if __name__ == "__main__":
    main()
