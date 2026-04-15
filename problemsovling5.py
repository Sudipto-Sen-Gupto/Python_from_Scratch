# just check even number by using continue keyword

number=int(input("Enter the number="))
i=1
while i<=number:
    if(i%2==1):
        i+=1
       
        continue
   
    print(i,"is an even number")
    i+=1