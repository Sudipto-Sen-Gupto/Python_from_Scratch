#function of list

#append()
numberList=[2,4,5,4]
numberList.append(7)
print(numberList)

#length function
print(len(numberList))

#sort list
newList=[2,8,9,3,6,4,2,5]
#newList.sort() ascending 
newList.sort(reverse=True) #descending
print(newList)

thirdList=['Litchi',"Lemon","Orange","Apple","Coconut","Date"]
thirdList.sort()
print(thirdList)

#reverse()
fourthList=[5,7,9,2,1]
fourthList.reverse()
print(fourthList)

#insert
fourthList.insert(3,8)
print(fourthList)

#remove()
fourthList.remove(9)  #find the number and remove it from the list
print(fourthList)

#pop()
fourthList.pop(0) #remove data according to index number
print(fourthList)

