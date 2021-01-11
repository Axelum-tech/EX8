avg=0
count = int(input("how many grades?"))

for n in range(1,count+1):
    grade=int(input(" enter grade " + str(n) + ": " ))
    avg += grade

avg = avg/count
avg = round(avg,1)

if avg>=7 and avg<8.5:
    print("the average grade is: " + str(avg)+ " bad student")
elif avg>=8.5 and avg<9.0:
    print("the average grade is: " + str(avg)+ " medium student")
elif avg>=9.0 and avg<10.0:
    print("the average grade is: " + str(avg)+ " good student")
elif avg<7.0:
    print("the average grade is: " + str(avg)+ " very bad student")


