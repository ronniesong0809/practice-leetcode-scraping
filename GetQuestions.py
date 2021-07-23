import json
import requests
import os
import time
from utils.runtime import runtime, runtime_withoutFucName

level = ["", "easy", "medium", "hard"]

@runtime
def getAllProblemsSaveAsJsonFile():
    url = "https://leetcode.com/api/problems/all/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "cookie": os.environ.get("LEETCODE_COOKIE")
    }
    r = requests.get(url=url, headers=headers)
    data = r.json()
    with open('data/apiProblemsAll.json', 'w') as f:
        json.dump(data['stat_status_pairs'], f)

def getTags(slug):
    url = "https://leetcode.com/graphql"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "cookie": os.environ.get("LEETCODE_COOKIE")
    }
    body = {
        "operationName": "getQuestionDetail",
        "variables": {
            "titleSlug": slug + ""
        },
        "query": "query getQuestionDetail($titleSlug: String!) {\n  isCurrentUserAuthenticated\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    questionTitle\n    questionTitleSlug\n    content\n    translatedContent\n    difficulty\n    stats\n    allowDiscuss\n    contributors {\n      username\n      profileUrl\n      __typename\n    }\n    similarQuestions\n    mysqlSchemas\n    randomQuestionUrl\n    sessionId\n    categoryTitle\n    submitUrl\n    interpretUrl\n    codeDefinition\n    sampleTestCase\n    enableTestMode\n    metaData\n    enableRunCode\n    enableSubmit\n    judgerAvailable\n    infoVerified\n    envInfo\n    urlManager\n    article\n    questionDetailUrl\n    libraryUrl\n    adminUrl\n    companyTags {\n      name\n      slug\n    }\n    companyTagStats\n    topicTags {\n      name\n      slug\n    }\n    __typename\n  }\n  interviewed {\n    interviewedUrl\n    companies {\n      id\n      name\n      slug\n      __typename\n    }\n    timeOptions {\n      id\n      name\n      __typename\n    }\n    stageOptions {\n      id\n      name\n      __typename\n    }\n    __typename\n  }\n  subscribeUrl\n  isPremium\n  loginUrl\n}\n"
    }
    r = requests.post(url=url, headers=headers, data=json.dumps(body))
    response = r.json()
    return response["data"]["question"]["topicTags"], json.loads(response["data"]["question"]["similarQuestions"]), response["data"]["question"]["companyTags"], json.loads(response["data"]["question"]["companyTagStats"]), response["data"]["question"]["envInfo"]

@runtime_withoutFucName
def buildData(x):
    x["tags"], x["similarQuestions"], x["companyTags"], x["companyTagStats"], temp = getTags(x["stat"]["question__title_slug"])
    x["difficulty"]["level"] = level[x["difficulty"]["level"]]

    del x["stat"]["question__article__slug"]
    del x["stat"]["question__article__live"]
    del x["stat"]["question__article__has_video_solution"]
    del x["status"]
    
    print(f'{x["stat"]["question_id"]} => [tags/similar/companies/stats]: {len(x["tags"])}/{len(x["similarQuestions"])}/{len(x["companyTags"])}/[{len(x["companyTagStats"]["1"])}/{len(x["companyTagStats"]["2"])}/{len(x["companyTagStats"]["2"])}] => {x["difficulty"]["level"]}', end="\t => ")

def preProcessing():
    with open("data/apiProblemsAll.json") as f:
        data = json.loads(f.read())
        with open("db/allQuestions.json", "w") as f:
            for x in data:
                buildData(x)

            json.dump(data, f)

def test():
    a, b, c, d, e = getTags("two-sum")

    with open("data/testing/topicTags.json", "w") as f:
        json.dump(a, f)

    with open("data/testing/similarQuestions.json", "w") as f:
        json.dump(b, f)

    with open("data/testing/companyTagStats.json", "w") as f:
        json.dump(c, f)

    with open("data/testing/companyTags.json", "w") as f:
        json.dump(d, f)

    with open("data/testing/envInfo.json", "w") as f:
        json.dump(json.loads(e), f)
    print("Done! → data/testing/")

@runtime
def run():
    getAllProblemsSaveAsJsonFile()
    # test()
    preProcessing()

def main():
    run()

if __name__ == "__main__":
    main()