import sys
import hanlp

HanLP = hanlp.load(hanlp.pretrained.mtl.UD_ONTONOTES_TOK_POS_LEM_FEA_NER_SRL_DEP_SDP_CON_XLMR_BASE)
sys.stdout = open("result_en_OntoNotes.txt", "w")

path = '//dataset/Data_en-GB.txt'
file = open(path, 'r')

sentences = file.readlines()
for sentence in sentences:
    doc = HanLP(sentence)
    doc.pretty_print()
    print("\n")

sys.stdout.close()

