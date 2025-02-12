import requests
from Valid import Valid

'''
Wi
'''
def main():
  userInput = ""
  while userInput != "quit":
    print("\n")
    userInput = input("Input: ")
    
    #zip is located in obj[3]
    if not Valid.zip(userInput):
      continue

    print("Valid")

  return #end main

if __name__ == '__main__':
  main()