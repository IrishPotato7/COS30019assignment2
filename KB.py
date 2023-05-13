def readKB(filename):
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if line == "TELL":
                line = file.readline().strip().replace(" ", "")
                kb = line.split(";")
                kb = list(filter(None, kb))
                print(kb)