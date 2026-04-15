
# just odd number check by using continue keyword

number=int(input("Enter the value="))
 
i=1

while i<number:
    if(i%2==0):
        i+=1
        continue #skip

    print(i,"is an odd number")

    i+=1
