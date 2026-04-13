detail={
    "name":"Gaurav Sen gupto",
    "Age":27,
    "CGPA":3.75,
    "Varsity":"Rabindra Maitree University",
    "Subjects":{
        "Operating_System":3.80,
        "Data_Structure_Algorithm":3.6,
        "Java_programming":4.00,
        "Computer_Networking":4.00
    }
    
}
detail["Region"]="Kushtia"
# print(list(detail.keys()))
# print(len(list(detail.keys())))
# print(detail.values())
# print(detail.items())
# print(detail.get('Varsity'))
# print(detail)
newDetail={"Division":"Khulna"}
detail.update(newDetail)
print(detail)