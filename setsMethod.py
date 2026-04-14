newSet=set ()
#add method
newSet.add(10)
newSet.add(20)
newSet.add(30)

print(newSet)
#remove method
newSet.remove(20)
print(newSet)

#clear method
# newSet.clear()
# print(newSet)

#pop method
newSet.pop()
print(newSet)

#union method

firstNumberSet={2,3,5,5,6}
secondNumberSet={3,7,8,9}
resultOfUnion=firstNumberSet.union(secondNumberSet)
print(resultOfUnion)

resultOfInterSection=firstNumberSet.intersection(secondNumberSet)
print(resultOfInterSection)

