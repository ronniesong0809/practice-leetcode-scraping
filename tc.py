import json

def dump(input, output):
  with open(input) as f:
    data = json.loads(f.read())
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
  dump("data/topics.json", "data/newTopics.json")
  dump("data/companies.json", "data/newCompanies.json")

if __name__ == "__main__":
  main()
