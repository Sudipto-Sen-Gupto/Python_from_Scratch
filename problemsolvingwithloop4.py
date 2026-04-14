#search for a number x in this tuple using loop
# [1,4,9,16,25,36,49,64,81,100]

tuple=(1,4,9,25,36,49,64,81,100)

x=int(input("Enter your searching value="))
i=0
while i<len(tuple):
    if(x==tuple[i]):
        print("Your searching number exist, found at index=",i)
        break
    i+=1
    
else:
 print("Your searching number does not exist in this tuple") 
       
