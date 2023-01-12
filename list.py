mylist = ["apple", "banana", "cherry"]

print(type(mylist))

print(len(mylist))

thislist = list(("Real Madrid", "FC barocellona", "PSG", "AC Milan", "Manchester United"))

print(thislist)

# print last item of thislist
print(thislist[-1])

print(thislist[2:5])

print(thislist[:4])

print(thislist[2:])

print(thislist[-4:-1])

if "PSG" in thislist:
    print("Yes")

thislist.insert(len(thislist), "Chelsea")

print(thislist)

thislist[1] = "Inter Milan"

thislist[2:4] = ["Bayern Munchen", "Borussia Dortmund"]
