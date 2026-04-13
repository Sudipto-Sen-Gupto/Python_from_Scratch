#object is known as dictionary in python 

biodata={
    "Name":"Gaurav Sen gupto",
    "Age":27,
    "CGPA":3.75,
    "Varsity_Name":"Ranbindra Maitree University",
    "Subject":{
        "CSE_1001":"Computer Fundamental",
        "CSE_1002":"Computer fundamental lab",
        "CSE_3101":"Operating System",
        "CSE_3102":"Operating System Lab"
    }
}
print(type(biodata))
print(biodata['Name'])    
print(biodata["Varsity_Name"],biodata["Subject"]["CSE_3102"])