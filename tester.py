import grammar
import sys

with open("error1.txt","r") as f:
    contents = f.read()

grammar.parser.parse(contents, tracking = True)
