#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    dirs = dir(hidden_4)

    for directory in dir:
        if directory[:2] == "__":
            continue
        print(directory)
