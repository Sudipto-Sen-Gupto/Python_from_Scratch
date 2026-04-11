#if elif else
the_year=int(input("Enter your desirable year="))
if(the_year%4==0 and the_year%100!=0):
    print("Leap year")

elif(the_year%400==0):
     print("Leap year")

else:{
    print("not leap year")
}