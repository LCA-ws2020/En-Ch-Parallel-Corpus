from pyhanlp import *
import sys

sys.stdout = open("anno_zh_tryout.txt", "w")

path = '//dataset/Data_zh-CN.txt'
file = open(path, 'r')

sentences = file.readlines()
for sentence in sentences:
    # tokenize each Chinese sentence
    print(HanLP.segment(sentence))

    # PoS tagging
    for term in HanLP.segment(sentence):
        # print each token and its part of speech
        print('{}\t{}'.format(term.word, term.nature))

    # Dependency parsing
    print(HanLP.parseDependency(sentence))

sys.stdout.close()