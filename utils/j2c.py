import json
import csv

data = []
with open('../data/data.json') as f:
    data = json.loads(f.read())
    f = csv.writer(open("../data/data.csv", "w", newline=''))

f.writerow(["question_id", "question_article_live", "question_article__has_video_solution", "question_title", "question_hide",
            "total_acs", "total_submitted", "is_new_question", "difficulty", "is_favor", "frequency", "progress"])

for x in reversed(data):
    f.writerow([x["stat"]["question_id"],
                x["stat"]["question__article__live"],
                x["stat"]["question__article__has_video_solution"],
                x["stat"]["question__title"],
                x["stat"]["question__hide"],
                x["stat"]["total_acs"],
                x["stat"]["total_submitted"],
                x["stat"]["is_new_question"],
                x["difficulty"]["level"],
                x["is_favor"],
                x["frequency"],
                x["progress"]])
