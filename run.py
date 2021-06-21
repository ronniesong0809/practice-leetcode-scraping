import json
import requests
import time
import random

def getTags(slug):
    url = "https://leetcode.com/graphql"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "cookie": "_ga=GA1.2.37052354.1606567733; __stripe_mid=8f3b50cb-b0df-4231-869f-056091828c2d36b551; csrftoken=NPIQLYahmRJrGm5gob0f9ZvUhColNdKs6ZFI76pEMJysFGG51y8eu8mk4Xzx4BbF; gr_user_id=66e7429a-be1e-46c8-b2dc-258ca871d86a; 87b5a3c3f1a55520_gr_last_sent_cs1=ronsong; _gid=GA1.2.755445100.1623913413; __atuvc=7%7C20%2C0%7C21%2C0%7C22%2C0%7C23%2C4%7C24; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMjExNzMzNyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImMwNzJmYzdkYjZjZmYyZDM2ZTk2YTg2MGUzY2VjODUwNGEyNmE2MzMiLCJpZCI6MjExNzMzNywiZW1haWwiOiJyb25zb25nQHBkeC5lZHUiLCJ1c2VybmFtZSI6InJvbnNvbmciLCJ1c2VyX3NsdWciOiJyb25zb25nIiwiYXZhdGFyIjoiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUuY29tL3VzZXJzL3JvbnNvbmcvYXZhdGFyXzE1OTkzMDg1NzYucG5nIiwicmVmcmVzaGVkX2F0IjoxNjIzOTc5MzI5LCJpcCI6IjczLjE4MC4xNy4yMTIiLCJpZGVudGl0eSI6IjM2NTFmMDcyMzk1MzQ3NTM3Yzc0MDg5OTg5Yzg4YTY2Iiwic2Vzc2lvbl9pZCI6ODcwMDM4NCwiX3Nlc3Npb25fZXhwaXJ5IjoxMjA5NjAwLCJjb252ZXJzaW9uX3RhcmdldHMiOnsiUnh0YVZ4RUtBUVJIR1VWUVNoZ1hGUU1VVEJRR0FCd0VEUXRCRkZkYlFGOGFIVkpRRmhzWEFnPT0iOnsic2VuZF9zZXNzaW9uX2lkcyI6WzE0NzJdLCJlbWFpbCI6InJvbnNvbmdAcGR4LmVkdSJ9LCJSeHRhVnhFS0FRUkhEMUJjRGdNTFhRc1hXMDBBSEFaZFdrd0hGZz09Ijp7InNlbmRfc2Vzc2lvbl9pZHMiOlsxNDcyXSwiZW1haWwiOiJyb25zb25nQHBkeC5lZHUifX19.gm-eklvbBhAMYPQRkHTtUbXszpSw_UZR9Hv31PYl6X0; __cf_bm=7ec5394c5d26c3786c6f5cdc34bd8cf440ed0278-1624081809-1800-AePpjgHeD/RkKDy6nACUffop2Ompd4Uw8SqvwCEi0AZNP302ITc0MHqlcWL0UHMezsoKmgEtHa/03ycMhmWwFNM=; _gat=1; 87b5a3c3f1a55520_gr_session_id=916960ad-419d-43ff-9738-96459e6e8857; 87b5a3c3f1a55520_gr_last_sent_sid_with_cs1=916960ad-419d-43ff-9738-96459e6e8857; 87b5a3c3f1a55520_gr_cs1=ronsong; 87b5a3c3f1a55520_gr_session_id_916960ad-419d-43ff-9738-96459e6e8857=true; c_a_u=cm9uc29uZw==:1luTsH:srVPMoSaXgjdxxkpRcBuBATDWrg"
    }
    body = {
        "operationName": "getQuestionDetail",
        "variables": {
            "titleSlug": slug+""
        },
        "query": "query getQuestionDetail($titleSlug: String!) {\n  isCurrentUserAuthenticated\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    questionTitle\n    questionTitleSlug\n    content\n    translatedContent\n    difficulty\n    stats\n    allowDiscuss\n    contributors {\n      username\n      profileUrl\n      __typename\n    }\n    similarQuestions\n    mysqlSchemas\n    randomQuestionUrl\n    sessionId\n    categoryTitle\n    submitUrl\n    interpretUrl\n    codeDefinition\n    sampleTestCase\n    enableTestMode\n    metaData\n    enableRunCode\n    enableSubmit\n    judgerAvailable\n    infoVerified\n    envInfo\n    urlManager\n    article\n    questionDetailUrl\n    libraryUrl\n    adminUrl\n    companyTags {\n      name\n      slug\n    }\n    companyTagStats\n    topicTags {\n      name\n      slug\n    }\n    __typename\n  }\n  interviewed {\n    interviewedUrl\n    companies {\n      id\n      name\n      slug\n      __typename\n    }\n    timeOptions {\n      id\n      name\n      __typename\n    }\n    stageOptions {\n      id\n      name\n      __typename\n    }\n    __typename\n  }\n  subscribeUrl\n  isPremium\n  loginUrl\n}\n"
    }
    r = requests.post(url=url, headers=headers, data=json.dumps(body))
    response = r.json()
    result = []
    result.append(response["data"]["question"]["topicTags"])
    result.append(response["data"]["question"]["similarQuestions"])
    result.append(response["data"]["question"]["companyTags"])
    result.append(response["data"]["question"]["companyTagStats"])
    result.append(response["data"]["question"]["envInfo"])
    return result

def cleaningTags(tags):
    for x in tags:
        del x["translatedTitle"]
    # print(tags)
    return tags

def run():
    with open("raw.json") as f:
        data = json.loads(f.read())
        with open("data.json", "w") as f:
            for x in data:
                response = getTags(x["stat"]["question__title_slug"])
                print(x["stat"]["question_id"], end=": ")
                print(response[0])
                x["tags"] = response[0]
                x["similarQuestions"] = cleaningTags(json.loads(response[1]))
                x["companyTags"] = response[2]
                x["companyTagStats"] = json.loads(response[3])
                del x["stat"]["question__article__slug"]
                del x["stat"]["question__article__live"]
                del x["stat"]["question__article__has_video_solution"]
                del x["status"]

            json.dump(data, f)

def test():
    response = getTags("two-sum")

    with open("testing/topicTags.json", "w") as f:
        json.dump(response[0], f)

    with open("testing/similarQuestions.json", "w") as f:
        json.dump(cleaningTags(json.loads(response[1])), f)

    with open("testing/companyTagStats.json", "w") as f:
        json.dump(json.loads(response[2]), f)

    with open("testing/companyTags.json", "w") as f:
        json.dump(response[3], f)

    with open("testing/envInfo.json", "w") as f:
        json.dump(json.loads(response[4]), f)

run()
# test()