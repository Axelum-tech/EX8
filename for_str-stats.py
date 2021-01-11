text="Hi! I like the for loop in Phyton. It took me a minute to understand it!"

count_prop=0

for c in text:
    if c in ".,!?":
        count_prop+=1

print("TEXT:", text)
print("total prop:", count_prop)