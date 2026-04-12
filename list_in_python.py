#list in object
data=[{
    "name":"Gaurav",
    "age":27,
    "Cgpa":3.75
},
{
    "name":"Prionty",
    "age":19,
    "Cgpa":3.5
}]

print(data)

list=["Iran","Israel","Iraq","Ireland","Iceland","Indonesia","India",4,29,48,28,48,57,10]
print("\n",list)
#list is mutable which means it can be changed, but string is immutable which means it can't be changed.
list[2]="Afghanistan"
print(list)

numberList=[3,5,7,9,0,4,5,6,6,6,7,8,9,0]
slicing=numberList[-8:-1]
print(slicing)
