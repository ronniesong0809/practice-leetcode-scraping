import json

with open('raw.json') as f:
    data = json.loads(f.read())

    with open('data.json', 'w') as f:
        for x in data:
          # print(x)
            del x["stat"]["question__article__slug"]
            del x["stat"]["question__title_slug"]
            del x["stat"]["frontend_question_id"]
            del x["status"]
        json.dump(data, f)
