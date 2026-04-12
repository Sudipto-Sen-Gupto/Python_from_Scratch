list=[1,2,2]
copyList=list.copy()
copyList.reverse()
if(list==copyList):
    print("Palindrome")
else:
    print("Not palindrome")