p=int(input("Enter the Principle amount:"))
n=int(input("Enter the number of years:"))
SC=input("Senior Citizen Yes/No:")
G=input("Male/Female:")
if SC=='Y' and G=='M':
    print("SI=",(p*n*12)/100)
elif SC=='Y' and G=='F':
    print("SI=",(p*n*15)/100)
else:
    print("SI=",(p*n*10)/100)
