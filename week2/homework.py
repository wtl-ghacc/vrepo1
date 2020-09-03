import logging
logging.basicConfig(level=logging.DEBUG)

def squared_threes():
    return_value = [range(0,100)]
    for i in return_value:
        
    # END SHOULDNT GO BEYOND HERE (PAST LINE 8)
    return return_value
    
if __name__ == "__main__":
    for x in squared_threes():
        print(x)
