import re
import KB

def TruthValue(kb, query):
    if query in kb:
        return [query]
    for argument in kb:
        argumentparams = re.split("&|=>", argument)
        if query != argumentparams[-1]:
            continue
        values =[]
        for statement in argumentparams[:-1]:
            value = TruthValue(kb, statement)
            if not value:
                return False
            elif statement in values:
                continue
            else:
                values = value + values
        values.append(query)
        return values      
    return False

def askBC(kb, query):
    result = TruthValue(kb, query)
    if result:
        result = ", ".join(result)
        print(f"YES: {result}")
    else:
        print("NO")

#kb, query = KB.readKB("test.txt")
#result = askBC(kb, query)