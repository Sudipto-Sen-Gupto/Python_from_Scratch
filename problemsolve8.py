#search for a number x in the tuple using loop
# (1,4,9,16,25,36,49,64,81,100)

tuple=(1,4,9,16,25,36,49,64,36,81,100)
x=int(input("Enter your desirable number="))

#by using index function/method
# for i in tuple:
#     if(i==x):
#         print("My desirable number found at index",tuple.index(i),"=",x)  

#by general searching same value multiple time

index=0

for i in tuple:
    if(i==x):
        print("Your value found at index=",index)
    index+=1