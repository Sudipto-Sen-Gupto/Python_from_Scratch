 ##new concept recursion

def recursion(number):
    if(number==0):
        return 
    print(number)
    recursion(number-1)
    print("End")
recursion(5)