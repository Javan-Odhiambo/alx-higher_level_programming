#!/usr/bin/python3
if __name__ == "__name__":
    import hidden_4 as hidden
    for i in dir(hidden):
        if not i.startswith("__"):
            print(i)