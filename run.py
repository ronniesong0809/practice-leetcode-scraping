import GetQuestions
import GetTags
import InsertToMongodb
from dotenv import load_dotenv
import time
from utils.runtime import runtime

def main():
  load_dotenv()
  
  start = time.time()
  GetQuestions.main()
  print(f'GetQuestions.main(): {runtime(start):.2f} sec')

  start = time.time()
  GetTags.main()
  print(f'GetTags.main(): {runtime(start):.2f} sec')

  start = time.time()
  InsertToMongodb.main()
  print(f'InsertToMongodb.main(): {runtime(start):.2f} sec')

if __name__ == "__main__":
  start = time.time()
  main()
  print(f'Run.main(): {runtime(start):.2f} sec')