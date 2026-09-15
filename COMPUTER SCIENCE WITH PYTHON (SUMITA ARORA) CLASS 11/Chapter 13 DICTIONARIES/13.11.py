#13.11
d1={1:11, 2:12}
d2={1:11, 2:12, 3:13, 4:15}
for i in d1:
    if i not in d2:
        print("d1 is not contained in d2")
        break
else:
    print("d1 is contained in d2")