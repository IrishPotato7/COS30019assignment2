import re

# Asks if a sentence is true by asking if the sentences that infer it are true
def TruthValue(kb, query):
    # Returns the query if it is true in the kb
    if query in kb:
        return [query]

    # Checks if the query is inferred in the argument
    for argument in kb:
        argumentparams = re.split("&|=>", argument)
        if query != argumentparams[-1]:
            continue

        # Runs this function for the statements in the argument
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

# Initiates the recursive TruthValue function
def askBC(kb, query):
    result = TruthValue(kb, query)
    if result:
        result = ", ".join(result)
        print(f"YES: {result}")
    else:
        print("NO")