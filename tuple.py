x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

(one, two, three) = x
print(one)
print(two)
print(three)

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

for i in range(len(thistuple)):
    print(thistuple[i])

i = 0;
while i < len(thistuple) - 1:
    print(thistuple[i])
    i += 1

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
