import GetQuestions
import GetTagsCompanies
import InsertToMongodb
from dotenv import load_dotenv
from utils.runtime import runtime

@runtime
def main():
  load_dotenv()

  GetQuestions.main()
  GetTagsCompanies.main()
  InsertToMongodb.main()

if __name__ == "__main__":
  main()