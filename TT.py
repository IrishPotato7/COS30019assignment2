import re
import itertools
import KB

# Create the truth table to analyse
def createTT(kb):
    statements = []
    tt = {}

    # Pull out the statements from the knowledge base
    for argument in kb:
        tempStatements = re.split("&|=>", argument)
        for tempStatement in tempStatements:
            if tempStatement not in statements:
                statements.append(tempStatement)

    # Generate an array of values to input into the truth table
    ttvalues = list(itertools.product([0, 1], repeat=len(statements)))

    # Add the statements with the associated values to the truth table
    for statement in statements:
        tt[statement] = []
    for values in ttvalues:
        i = 0
        for value in values:
            tt[statements[i]].append(value)
            i += 1

    for argument in kb:
        if "=>" in argument:
            tt[argument] = []
            argumentparams = re.split("&|=>", argument)
            for i in range(len(ttvalues)):
                argumentvalue = 1
                if tt[argumentparams[-1]][i] == 0:
                    argumentsvalues = []
                    for argumentparam in argumentparams[:-1]:
                        argumentsvalues.append(tt[argumentparam][i])
                    if all(argumentsvalues):
                        argumentvalue = 0
                tt[argument].append(argumentvalue)

    finalstatement = "^".join(kb)
    tt[finalstatement] = []
    for i in range(len(ttvalues)):
        argumentvalue = 1
        for argument in kb:
            if tt[argument][i] == 0:
                argumentvalue = 0
        tt[finalstatement].append(argumentvalue)

    return tt

# Ask the truth table the query
def askTT(tt, query):
    count = 0
    kb = list(tt)[-1]

    # Check if the query is true when the kb is true
    # If the kb is true and the query is not true the function returns
    # If both are true, counts how many times both are true
    for i in range(len(tt[kb])):
        if tt[kb][i] == 1:
            if tt[query][i] == 0:
                print("NO")
                return
            else:
                count += 1

    print("YES:", count)
    return


kb, query = KB.readKB("test.txt")
tt = createTT(kb)
askTT(tt, query)
