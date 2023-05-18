import sys
import KB
import TT

def main():
    try:
        method = sys.argv[1]
        filename = sys.argv[2]

    except:
        print("Invalid command, please enter the method followed by the file")
        method = input("Enter name of method to use:")
        filename = input("Enter name of file to read:")

    kb, query = KB.readKB(filename)
    tt = TT.createTT(kb)
    
    if method == "TT":#py main.py TT test.txt
        print("Truth table runs")
        TT.askTT(tt, query)
    elif method == "FC":#py main.py FC test.txt
        print("Forward chaining runs")
    elif method == "BC":#py main.py BC test.txt
        print("Backward chaining runs")
    else:
        print("Invalid method, please enter 'TT', 'FC', or 'BC'.")



if __name__ == "__main__":
    main()