import logging
logging.basicConfig(level=logging.DEBUG)

def squared_threes():
    return_value = [3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60,63,66,69,72,75,78,81,84,87,90,93,96,99]
    for i in return_value:
        print(i**2)

    return return_value
    
if __name__ == "__main__":
    for x in squared_threes():
        print(x)
