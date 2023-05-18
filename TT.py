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
    size = range(len(ttvalues))

    # Add the statements with the associated values to the truth table
    for statement in statements:
        tt[statement] = []
    for values in ttvalues:
        for i, value in enumerate(values):
            tt[statements[i]].append(value)

    # Add the arguments to the truth table and evaluate them
    for argument in kb:
        if "=>" in argument:
            tt[argument] = []
            argumentparams = re.split("&|=>", argument)
            for i in size:
                argumentvalue = 1
                if tt[argumentparams[-1]][i] == 0:
                    argumentsvalues = []
                    for argumentparam in argumentparams[:-1]:
                        argumentsvalues.append(tt[argumentparam][i])
                    if all(argumentsvalues):
                        argumentvalue = 0
                tt[argument].append(argumentvalue)

    # Add the kb to the truth table and evaluate it
    finalstatement = "^".join(kb)
    tt[finalstatement] = []
    for i in size:
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
    for i, value in enumerate(tt[kb]):
        if value == 1:
            if tt[query][i] == 0:
                print("NO")
                return
            else:
                count += 1

    print(f"YES: {count}")
    return

#kb, query = KB.readKB("test.txt")
#tt = createTT(kb)
#askTT(tt, query)
