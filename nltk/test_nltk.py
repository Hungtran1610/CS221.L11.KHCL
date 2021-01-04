import nltk
from nltk.parse.corenlp import CoreNLPParser

rules = []
result = []

file = open('./grammar.txt')
lines = file.readlines()
rules = ''.join(lines)

grammar = nltk.CFG.fromstring(rules)

inputs = open('./Data/test.txt')
input_lines = inputs.readlines()

parser = nltk.EarleyChartParser(grammar)
f = open("./Data/output_nltk.txt", "w")

for line in input_lines:
    INDEX = 0
    for tree in parser.parse(line.split()):
        if INDEX == 1:
            continue
        result.append(str(tree.pformat()) + '\n')
        f.writelines(str(tree.pformat()))
        INDEX += 1

f.close()
print(result)