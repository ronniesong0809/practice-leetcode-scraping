import json
import requests

def getJsonFile():
    url = "https://leetcode.com/problems/api/tags/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "cookie": "csrftoken=BWKWNm168hUWzwct5SagwtOLGfMP6J0oTaJbFQKaKgWAlBKzQK40rtAJlyoDtcF1; _ga=GA1.2.1056492324.1616526906; gr_user_id=e725893a-db5a-476b-ba83-08c98167e867; __stripe_mid=3178cb88-d3d0-4f83-9baf-422cdbf2bedbf127b1; 87b5a3c3f1a55520_gr_last_sent_cs1=ronsong; _gid=GA1.2.921365914.1623575440; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMjExNzMzNyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImMwNzJmYzdkYjZjZmYyZDM2ZTk2YTg2MGUzY2VjODUwNGEyNmE2MzMiLCJpZCI6MjExNzMzNywiZW1haWwiOiJyb25zb25nQHBkeC5lZHUiLCJ1c2VybmFtZSI6InJvbnNvbmciLCJ1c2VyX3NsdWciOiJyb25zb25nIiwiYXZhdGFyIjoiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUuY29tL3VzZXJzL3JvbnNvbmcvYXZhdGFyXzE1OTkzMDg1NzYucG5nIiwicmVmcmVzaGVkX2F0IjoxNjI0NTgxNzU1LCJpcCI6IjczLjE4MC4xNy4yMTIiLCJpZGVudGl0eSI6IjcyNzY2YWIyYjFjODVhZjk4YWRiYmI5NjgzNjAwZmRmIiwic2Vzc2lvbl9pZCI6NzM3MTMyMCwiX3Nlc3Npb25fZXhwaXJ5IjoxMjA5NjAwfQ.i6BAkNg1mnMoN8tt013jpAEy0mKxzmuQdM72DvhEtkg; __atuvc=4|21,4|22,2|23,18|24,4|25; NEW_PROBLEMLIST_PAGE=1; 87b5a3c3f1a55520_gr_cs1=ronsong; c_a_u=cm9uc29uZw==:1lwyyP:IxW1GCRlnb1LfVKaAFaUJXLWjf4; __cf_bm=f5ccb1d961f2abfb53c92fadcb1b33df6d40fb4e-1624681951-1800-AVQIt0jg9Zr4E09DQUdqw/uF1MevR03csKdhcE5YvWUPf+csTuXtto1gCis9tb7H6zlxxentZ7B50aPLhqxFQeM="
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
