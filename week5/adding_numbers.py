import sys
def add_them_all(filename):
    sum = 0
    numbersFile = open("data.txt", "r") # replace data.txt with a.txt, b.txt, etc. or the directory/path the datafile is located, e.g. C:\\numbers\a.txt
    for line in numbersFile:
        sum = sum + int( line )
    return sum
if __name__ == "__main__":
    fname = sys.argv[1]
    print(f"Processing {fname}")
    print(add_them_all(fname))
