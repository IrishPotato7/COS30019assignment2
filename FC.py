#The new FC


import re
import KB

#Add values to the queue list based on the sentences that are known to be true
def findRules(kb):
    rule =[]
    queue =[]
    checkedTrue=[]
    #Add first rules (eg. a, b, p2)
    for argument in kb:
        argumentparams = re.split("&|=>", argument)  
        if argumentparams[0]==argumentparams[-1]:
            rule.append(argumentparams[0])
            checkedTrue.append(argumentparams[0])
    return rule, queue, checkedTrue

#If LHS of sentence is in queue list, add RHS of sentence to queue
def TruthValue(checkedTrue, queue, kb, query):
    
    if query in checkedTrue:
        return queue
    for argument in kb:
        argumentparams = re.split("&|=>", argument)
        if queue is False:
            return
        elif query in queue:
            return queue
        try:
            if argumentparams[0] in checkedTrue and argumentparams[-2] in checkedTrue and argumentparams[-1] not in queue:
                queue.append(argumentparams[-1])
                checkedTrue.append(argumentparams[-1])
                queue = TruthValue(checkedTrue, queue, kb, query)
                continue
        except:
            queue=[]
            return False

def askFC(kb, query):
    rule, queue, checkedTrue = findRules(kb)
    result = TruthValue(checkedTrue, queue, kb, query)
    if result is not False :
        result = rule + result
        result = ", ".join(result)
        print(f"YES: {result}")
    else:
        print("NO")

#kb, query = KB.readKB("test.txt")
#result = askFC(kb, query)