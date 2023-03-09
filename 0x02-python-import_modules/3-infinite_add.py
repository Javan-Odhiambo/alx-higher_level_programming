#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    l = [int(x) for x in sys.argv[1:]]
    print("{}".format(sum(l)))
