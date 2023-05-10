def readKB(filename):
    with open(filename) as file:
        for line in file:
            print(line)

readKB('test.txt')