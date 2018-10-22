#!/usr/bin/python3
import json


#   word      next   probability
# {"hello": {"word": 100%}}
def generate_dict(text, save_as):
    with open(text, "r") as f:
        print(f.read())

def generate_sentence():
    pass

def main():
    print("main")
    generate_dict("generic.txt")

if __name__ == "__main__":
    main()
