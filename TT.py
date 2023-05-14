import re
import itertools
import KB

def createTT(kb, query):
    statements = []
    ttstatements = {}
    for argument in kb:
        tempStatements = re.split("&|=>", argument)
        for tempStatement in tempStatements:
            if tempStatement not in statements:
                statements.append(tempStatement)
    ttvalues = list(itertools.product([0, 1], repeat=len(statements)))
    for statement in statements:
        ttstatements[statement] = []
    for values in ttvalues:
        i = 0
        for value in values:
            ttstatements[statements[i]].append(value)
            i += 1

kb, query = KB.readKB("test.txt")
createTT(kb, query)