import json
import requests
import time
import random

def getTags(slug):
    url = "https://leetcode.com/graphql"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    body = {
        "operationName": "getQuestionDetail",
        "variables": {
            "titleSlug": slug+""
        },
        "query": "query getQuestionDetail($titleSlug: String!) {\n  isCurrentUserAuthenticated\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    questionTitle\n    translatedTitle\n    questionTitleSlug\n    content\n    translatedContent\n    difficulty\n    stats\n    allowDiscuss\n    contributors {\n      username\n      profileUrl\n      __typename\n    }\n    similarQuestions\n    mysqlSchemas\n    randomQuestionUrl\n    sessionId\n    categoryTitle\n    submitUrl\n    interpretUrl\n    codeDefinition\n    sampleTestCase\n    enableTestMode\n    metaData\n    enableRunCode\n    enableSubmit\n    judgerAvailable\n    infoVerified\n    envInfo\n    urlManager\n    article\n    questionDetailUrl\n    libraryUrl\n    adminUrl\n    companyTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    companyTagStats\n    topicTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    __typename\n  }\n  interviewed {\n    interviewedUrl\n    companies {\n      id\n      name\n      slug\n      __typename\n    }\n    timeOptions {\n      id\n      name\n      __typename\n    }\n    stageOptions {\n      id\n      name\n      __typename\n    }\n    __typename\n  }\n  subscribeUrl\n  isPremium\n  loginUrl\n}\n"
    }
    r = requests.post(url=url, headers=headers, data=json.dumps(body))
    response = r.json()
    return response["data"]["question"]["topicTags"]

def cleaningTags(tags):
    for x in tags:
        del x["translatedName"]
        del x["__typename"]
    print(tags)
    return tags

with open("raw.json") as f:
    data = json.loads(f.read())
    with open("data.json", "w") as f:
        for x in data:
            tags = getTags(x["stat"]["question__title_slug"])
            cleanTags = cleaningTags(tags)
            x["tags"] = cleanTags
            del x["stat"]["question__article__slug"]
            del x["stat"]["frontend_question_id"]
            del x["status"]

        json.dump(data, f)
