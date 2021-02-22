import sys
import hanlp

HanLP = hanlp.load(hanlp.pretrained.mtl.OPEN_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_BASE_ZH)
sys.stdout = open("result_en_OpenCh.txt", "w")

path = '//dataset/Data_en-GB.txt'
file = open(path, 'r')

sentences = file.readlines()
for sentence in sentences:
    doc = HanLP(sentence)
    doc.pretty_print()
    print("\n")

sys.stdout.close()