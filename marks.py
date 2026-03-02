r=int(input("enter the marks:"))
if r>=90:
    print("grade is A")
elif(r<90 and r>=80):
    print("grade is B")
elif(r<80 and r>=70):
    print("grade is C")
elif(r<70 and r>=60):
    print("grade is D")
else:
    print("grade is F")