import sys
import KB
import TT
import FC
import BC

def main():
    try:
        method = sys.argv[1]
        filename = sys.argv[2]
    except Exception:
        print("Invalid command, please enter the method ('TT', 'FC', or 'BC') followed by the file name")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")

    kb, query = KB.readKB(filename)
    
    if method == "TT":#py main.py TT test.txt
        print("Truth table method runs")
        TT.askTT(kb, query)
    elif method == "FC":#py main.py FC test.txt
        print("Forward chaining method runs")
        FC.askFC(kb, query)
    elif method == "BC":#py main.py BC test.txt
        print("Backward chaining method runs")
        BC.askBC(kb, query)
    else:
        print("Invalid method, please enter 'TT', 'FC', or 'BC'.")



if __name__ == "__main__":
    main()