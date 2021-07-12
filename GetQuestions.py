import json
import requests
import os

def getJsonFile():
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

def getDifficulty(level):
    if level == 1:
        return "easy"
    elif level == 2:
        return "medium"
    elif level == 3:
        return "hard"

def run():
    with open("data/apiProblemsAll.json") as f:
        data = json.loads(f.read())
        with open("db/allQuestions.json", "w") as f:
            for x in data:
                response = getTags(x["stat"]["question__title_slug"])
                print(x["stat"]["question_id"], end=": ")
                print(response[0], end=" => ")
                x["tags"] = response[0]
                x["similarQuestions"] = cleaningTags(json.loads(response[1]))
                x["companyTags"] = response[2]
                x["companyTagStats"] = json.loads(response[3])
                x["difficulty"]["level"] = getDifficulty(x["difficulty"]["level"])
                print(len(x["similarQuestions"]), end="/")
                print(len(x["companyTags"]), end="/")
                print(len(x["companyTagStats"]), end=" => ")
                print(x["difficulty"]["level"])
                del x["stat"]["question__article__slug"]
                del x["stat"]["question__article__live"]
                del x["stat"]["question__article__has_video_solution"]
                del x["status"]

            json.dump(data, f)

def test():
    response = getTags("two-sum")

    with open("data/testing/topicTags.json", "w") as f:
        json.dump(response[0], f)

    with open("data/testing/similarQuestions.json", "w") as f:
        json.dump(cleaningTags(json.loads(response[1])), f)

    with open("data/testing/companyTagStats.json", "w") as f:
        json.dump(response[2], f)

    with open("data/testing/companyTags.json", "w") as f:
        json.dump(json.loads(response[3]), f)

    with open("data/testing/envInfo.json", "w") as f:
        json.dump(json.loads(response[4]), f)
    print("Done! → data/testing/")

def main():
    getJsonFile()
    # test()
    run()

if __name__ == "__main__":
    main()