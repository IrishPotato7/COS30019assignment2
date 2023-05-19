import re
import KB

#Add values to the queue list based on the sentences that are known to be true
def findRules(kb):
    queue =[]
    #Add first rules (eg. a, b, p2)
    for argument in kb:
        argumentparams = re.split("&|=>", argument)  
        if argumentparams[0]==argumentparams[-1]:
            queue.append(argumentparams[0])
    return queue

#If LHS of sentence is in queue list, add RHS of sentence to queue
def TruthValue(queue, kb, query):
    if query in kb:
        return [query]
    for argument in kb:
        argumentparams = re.split("&|=>", argument)
        if query in queue:
            return queue
        elif argumentparams[0] in queue and argumentparams[-2] in queue and argumentparams[-1] not in queue:
            queue.append(argumentparams[-1])
            queue = TruthValue(queue, kb, query)
    return False

def askFC(kb, query):
    values = findRules(kb)
    result = TruthValue(values, kb, query)
    if result:
        result = ", ".join(result)
        print(f"YES: {result}")
    else:
        print("NO")

#kb, query = KB.readKB("test.txt")
#result = askFC(kb, query)