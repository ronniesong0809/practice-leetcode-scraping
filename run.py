import GetQuestions
import GetTags
import InsertToMongodb
from dotenv import load_dotenv

def main():
  load_dotenv()
  
  GetQuestions.main()
  GetTags.main()
  InsertToMongodb.main()

if __name__ == "__main__":
  main()