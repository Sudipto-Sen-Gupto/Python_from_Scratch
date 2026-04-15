#print the multiplication table of a number n

n=int(input("Enter your num"))

for i in range(1,11):
    multiplication=n*i
    print(i,"*",n,"=",multiplication)