#Enter marks of three subjects from the use and store them into dictionary .Start with an empty dictionary and add one by one .Use subject name as key and mark as value
Dictionary={}


MathMark=int(input("Enter your math marks="))

Dictionary["Math"]=MathMark
print(Dictionary)

PhysicsMark=int(input("Enter your pysics marks="))
Dictionary.update({"Physics":PhysicsMark})
print(Dictionary)

BiologyMark=int(input("Enter your biology mark"))

Dictionary.update({"Biology":BiologyMark})
print(Dictionary)