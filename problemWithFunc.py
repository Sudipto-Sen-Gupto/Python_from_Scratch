##print the length of the list. list is the parameter

def lengthOfList(list):
    length=len(list)
    print("Length of the list",length)
    return length
lengthOfList([3,5,6,2,35,3])

## print the elements of list in a single line.list is the parameter
def elementsOfList(list):
     for x in list:
          print(x,end=",")
     print()
          

cities=['Dhaka',"Kushtia","Barisal","Rangpur","Pabna","Rajsahi","Rajbari"]
elementsOfList(cities)

##find the factorial of n . n is a parameter

def findFactorialNum(n):
    initialValue=1
    for x in range(1,n+1):
          initialValue*=x
          
    print("Factorial=",initialValue)
    return initialValue
findFactorialNum(5)


##Convert USD to TAKA

def converter (amount):
     taka=amount*100
     print("Convert usd dollar",amount,"into",taka,"bangladeshi tk")
     return
converter(67)

##take a number and check if the number is even print "even" if the number is odd print "odd"

def OddEvenCheck(number):
     if(number%2==0):
          print("Even")
     elif(number%2==1):
          print("Odd")
     else: print("Not a number")
OddEvenCheck(67)