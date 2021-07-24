import os
import requests
import json
from utils.runtime import runtime, runtime_withoutFucName
from threading import Thread
from queue import Queue
from random import randint
from time import sleep

class Spider:
    def __init__(self):
        self.level = ["", "easy", "medium", "hard"]
        self._queue = Queue()
        self.data = list()
        self.threadNum = 10
        self.timeoutCounter = 0

    @runtime
    def getAllProblemsSaveAsJsonFile(self):
        url = "https://leetcode.com/api/problems/all/"
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "cookie": os.environ.get("LEETCODE_COOKIE")
        }
        r = requests.get(url=url, headers=headers)
        
        data = r.json()
        new = [x for x in reversed(data["stat_status_pairs"])]
        with open("data/apiProblemsAll.json", "w") as f:
            json.dump(new, f)

    def processResponse(self, slug, id):
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
        sleep(randint(0,1))
        r = requests.post(url=url, headers=headers, data=json.dumps(body))

        if r.status_code == 200:
            print(f'[{r.status_code}] {id:>5}', end=" => ")
            response = r.json()
            return response["data"]["question"]["topicTags"], json.loads(response["data"]["question"]["similarQuestions"]), response["data"]["question"]["companyTags"], json.loads(response["data"]["question"]["companyTagStats"]), response["data"]["question"]["envInfo"]
        else:
            self.timeoutCounter = self.timeoutCounter + 1
            sleep(randint(10,15))
            print(f'[{r.status_code}] {id:>5}')
            return self.processResponse(slug, id)

    @runtime_withoutFucName
    def parsedata(self, x):
        slug = x["stat"]["question__title_slug"]
        id = x["stat"]["question_id"]

        x["tags"], x["similarQuestions"], x["companyTags"], x["companyTagStats"], temp = self.processResponse(slug, id)
        x["difficulty"]["level"] = self.level[x["difficulty"]["level"]]

        del x["stat"]["question__article__slug"]
        del x["stat"]["question__article__live"]
        del x["stat"]["question__article__has_video_solution"]
        del x["status"]
        
        print(f'[tags/similar/companies/stats]: {len(x["tags"])}/{len(x["similarQuestions"])}/{len(x["companyTags"])}/[{len(x["companyTagStats"]["1"])}/{len(x["companyTagStats"]["2"])}/{len(x["companyTagStats"]["2"])}] => {x["difficulty"]["level"]}', end=" => ")
        
    def buildQueue(self):
        with open("data/apiProblemsAll.json") as f:
            data = json.loads(f.read())
            for question in data:
                self._queue.put(question)

    def get_info(self):
        while not self._queue.empty():
            question = self._queue.get()
            self.parsedata(question)
            self.data.append(question)

    def preProcessing(self):
        self.buildQueue()
        
        ths = []
        for _ in range(self.threadNum):
            th = Thread(target=self.get_info)
            th.start()
            ths.append(th)
        for th in ths:
            th.join()

        print(f'Total 429 Timeout: {self.timeoutCounter}')
        print(f'Total Data Number: {len(self.data)}')

        s = json.dumps(self.data, ensure_ascii=False, indent=4)
        with open("db/allQuestions.json", "w", encoding="utf-8") as f:
            f.write(s)

    @runtime
    def run(self):
        self.getAllProblemsSaveAsJsonFile()
        self.preProcessing()

if __name__ == "__main__":
    Spider.run()