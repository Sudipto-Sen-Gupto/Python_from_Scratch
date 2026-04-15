#string find by using for loop

string="awesome"

for i in string:
    if(i=="s"):
     print(i,"found")
     break
    else:
       print(i,"Not a desired letter")