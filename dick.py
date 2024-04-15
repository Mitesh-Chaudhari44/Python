d = {
    100 : "Rohit",
    200 : "Dhoni",
    500 : "Kohli"
}

l1 = list(d.keys())
l2 = list(d.values())

temp = 0
for i in range(len(l1)):
    if l1[i] > temp:
        temp = l1[i]
        a = i

print("Skipper is : ", l2[a])
