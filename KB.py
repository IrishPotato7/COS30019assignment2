# Create the knowledge base from a txt file
def readKB(filename):
    with open(filename) as file:
        for line in file:
            line = line.strip()

            # Read in the knowledge base
            if line == "TELL":
                line = file.readline().strip().replace(" ", "")
                kb = line.split(";")
                kb = list(filter(None, kb))

            # Read in the query to ask
            elif line == "ASK":
                line = file.readline()
                query = line.strip()

    return kb, query