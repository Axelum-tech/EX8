
sms="Hi! My phone number is 01234567, call me and blah!"
for c in sms :
    if c=="0" or c=="1"or c=="2"or c=="3"or c=="4"or c=="5"or c=="6"or c=="7"or c=="8"or c=="9":
        print("*", end="")
    else:
        print(c, end="")