#sets

setNumber={1,3,3,"dip","dip",5,4,} #sets doest allow duplicate value
print(setNumber)
print(len(setNumber))

firstSet={2,3,5}
secondSet={3,4,5}
result=firstSet & secondSet  # & plays role as intersection
result2=firstSet | secondSet # | plays role as union
print(result)
print(result2)

emptySet={} # when the set contains element we can store it in curly brace but if the set empty then we can not write {} for empty set because {} considers as dictionary;
print(type(emptySet))
#so we can use set function for define empty set
newEmptySet=set({})
print(type(newEmptySet))